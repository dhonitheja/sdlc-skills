# Incident notes: checkout outage

- 14:02  Sam deployed release 2.9 to production (no canary, deployed all at once).
- 14:05  Error-rate alert fired. It paged the on-call for the search team, not the checkout team.
- 14:20  Checkout on-call noticed by customer reports in support chat. Started investigating.
- 14:45  Identified a bad database migration in 2.9 (index dropped on orders table).
- 15:10  Rollback of 2.9 completed. Errors stopped at 15:12.
- Impact: checkout requests failed for about 70 minutes (14:02 to 15:12). 12% of all API requests errored during that time.
- Sam should have been more careful with the migration.
- Customers affected: unknown, still being counted.
