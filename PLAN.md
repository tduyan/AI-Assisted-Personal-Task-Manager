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
