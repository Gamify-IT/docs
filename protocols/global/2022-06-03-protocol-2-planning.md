# Meeting Transcript 03.06.2022, 17:30

- present: Aaron, Gilian, Jonathan, Leon H, Martin, Max, Timo, Levi + Coaches
- absent: Leon L, Ilijaz
- excused: Michael, Florian

## Sprint 2 planning

- Recap: sprint goal ([2022-06-03-protocol-1.md](./2022-06-03-protocol-1.md))
- Discussion: Hierarchy for tasks
  - We want at most two levels (e.g. Epics and Tasks)
  - Should the epics permanently be in progress?
- Should we use separate databases for the different micro services?
- We tried out <https://scrumpoker.online> to do planning poker
  - The page went offline before we could estimate anything
- We used <https://www.scrumpoker-online.org> to estimate our tasks
- Estimated our tasks
- We cannot estimate the Unity Seminar without Ilijaz
- Many tasks require Unity knowledge to estimate
- The tasks that we can not estimate yet, will be estimated in another meeting
- Passwords are now managed in the [secrets repository](https://github.com/Gamify-IT/secrets)

## Follow-up actions

- New ADR: [Where do we create our Tasks/Issues?](../../adr/issues-repository.md) - We create all tasks in the Issues repo.
- New ADR [Should each service use their own database](../../adr/databases.md) (container)?
- Workflow in our sprint board (TODO: document this)
  - New tasks go into "Backlog" column
  - When they are refined and estimated, we drag them into "Ready for another sprint"
  - "Todo" contains the tasks selected for the sprint
  - During the sprint, completed tasks go into "Ready for Review" column
