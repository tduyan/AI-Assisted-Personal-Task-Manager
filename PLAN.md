# **Task Data Model**
| Field             | Type           | Required | Notes
| :-----------------| :-------------:| :-------:| -------------------------------------------------------------------:|
| `id`              | UUID/string    |      yes | Unique, generated on creation never reused
| `title`           | string         |      yes | 1-200 chars no empty/whitespace-only strings
| `description`     | string         |       no | Max ~1000 chars
| `status`          | enum           |      yes | `incomplete`, `complete` (add `archived` if you support soft-delete)
| `created_at`      | timestamp      |      yes | Set once, immutable
| `updated_at`      | timestamp      |      yes | Updated on every write
| `completed_at`    | timestamp      |       no | Null until marked complete; cleared if uncompleted
| `due_date`        | date/timestamp |       no | Nullable
| `reminder_at`     | timestamp      |       no | Nullable independent of due_date
| `priority`        | enum           |       no | `low`, `medium`, `high`, or null
| `list_id`         | reference      |      yes | FK to a list/category; falls back to a default list
| `recurrence_rule` | object/string  |       no | Null for one-off tasks; RRULE-style string works well
| `parent_task_id`  | reference      |       no | For recurring task instances, links back to the template
| `sort_order`      | number         |       no | For manual drag-reordering, if you support it
| `deleted_at`      | timestamp      |       no | Nullable - supports soft delete/trash

## **Edge Cases**
- Add a Task
  * Empty or whitespace-only title submitted
  * Title exceeds max length (truncate, reject, or warn - pick one and be consistent).
  * Duplicate title added twice in a row - is that allowed (Usually yess, task managers aren't supposed to dedupe by title.)
  * User adds a task while offline - needs to queue and sync later, not fail silently.
  * Rapid double-tap on "Add" creates two identical tasks.
  * Task added with a due date in the past - allow it, but (maybe) flag it as already-overdue on creation
  * `list_id` references a list that was deleted mid-session (race condition on shared devices/multi-tab)
- Mark a task complete
  * Marking complete on a task that's part of a recurring series - does it complete just this instance, or the whole series? (Needs a decision, covered in the recurrence logic.)
  * Un-completing a task - does `completed_at` get cleared, or kept for history?
  * Marking complete while offline, then the same task gets edited on another device before sync - conflict resolution needed.
  * Bulk-complete action (if supported) partially fails halfway through - which tasks ended up complete?
  * Completing a task triggers the next recurrence - what if generating the next instance fails? You don't want to lose the completion because a downstream step broke.
  * Task has a pending reminder - does completing it cancel the scheduled notification? (It should)
- Delete a task
  * Deleting a task that's mid-edit on another device.
  * Deleting a recurring task's template - does it delete future instances, past instances, or just detach them?
  * Deleting the last task in a list - does the list itself get cleaned up, or stay empty?
  * Accidental delete - is there an undo window or trash, or is it permanent? (Permanent - only deletes are a common source of support tickets.)
  * Deleting while offline, then the device reconnects and finds the task was also edited elsewhere - deletion should generally win, but that's a product decision, not just a technical one.
  * Cascading references: if `parent_task_id` or `list_id` pointed at the deleted task, those need to be cleaned up or nulled out, not left dangling.
- Save tasks between sessions (persistence)
  * App killed mid-write (crash, force-quit, low battery) - partial write shouldn't corrupt the task store.
  * Storage quota exceeded (especially relevant for local-first/offline storage on mobile).
  * Schema changes between app versions - old saved data needs a migration path, not a crash on load.
  * Concurrent writes from two tabs/windows of the same account.
  * Sync conflict: same task edited offline on two devices, both come back online - last-write winds is simplest but loses data; a merge or prompt is safer.
  * Corrupted local cache on load - app should recover smoothly (reload from server, or show an error) rather than losing the whole list.
  * Clock skew between device and server messing up `updated_at` comparisons during conflict resolution.
