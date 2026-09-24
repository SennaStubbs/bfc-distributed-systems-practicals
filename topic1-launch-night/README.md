# Launch Night

A new online game has launched and thousands of players are trying to connect. It uses several services, including a login service, a realm server and an Auction House.

In this activity, you’ll make a few small changes to a working Python program. You’ll run and test each change before using Git to record your work and push it to GitHub.

If you haven’t forked and cloned the practical repository yet, complete the **Getting Started with GitHub and Visual Studio Code** page on Canvas first.

## Stage 1: Run the Program

Open:

```text
launch_night.py
```

Select the **Run Python File** button in the top-right corner of Visual Studio Code.

You should see:

```text
LAUNCH NIGHT SERVICE MONITOR
============================
Login Service: online
Realm Server: online
Auction House: offline

Offline services: 0
```

The program works, but the final count is wrong. There is one offline service, not zero. You’ll fix that shortly.

If the Run button is missing, install the **Python** extension published by Microsoft. Visual Studio Code may suggest this automatically in the bottom-right corner.

## Stage 2: Look at the Service Data

Find `game_services` near the top of `launch_night.py`:

```python
game_services = [
    {"name": "Login Service", "status": "online"},
    {"name": "Realm Server", "status": "online"},
    {"name": "Auction House", "status": "offline"}
]
```

`game_services` is a list containing three dictionaries. Each dictionary describes one game service.

For example:

```python
{"name": "Login Service", "status": "online"}
```

This dictionary contains two key-value pairs:

- `name` has the value `"Login Service"`.
- `status` has the value `"online"`.

Each service uses the same two keys but stores different values.

## Stage 3: Add Another Service

Add this dictionary underneath the Auction House:

```python
{"name": "In-game Mail", "status": "online"}
```

Remember to add a comma after the Auction House dictionary.

Your finished list should look like this:

```python
game_services = [
    {"name": "Login Service", "status": "online"},
    {"name": "Realm Server", "status": "online"},
    {"name": "Auction House", "status": "offline"},
    {"name": "In-game Mail", "status": "online"}
]
```

Save the file and run it again using the **Run Python File** button.

You should now see:

```text
In-game Mail: online
```

If you get a syntax error, check your commas, quotation marks and brackets.

## Stage 4: Make Your First Commit

You’ve made and tested a useful change, so it’s time to commit it.

Open **Terminal → New Terminal** and run:

```bash
git status
```

You should see that `launch_night.py` has changed.

Now run:

```bash
git add .
git commit -m "Add in-game mail service"
git push
```

If Git asks you to configure `user.name` and `user.email`, return to the Getting Started page on Canvas.

Visual Studio Code may open GitHub in your browser and ask you to sign in. Use the account that owns your fork.

Once the push has finished, refresh your fork on GitHub and check that the new service appears in `launch_night.py`.

## Stage 5: Fix the Offline Count

Find this function:

```python
def count_offline无需_services(services):
    """Count and return the number of offline services."""
    # TODO: Replace the line below by following Stage 5 in README.md.
    return 0
```

Remove the `return 0` line and replace it with:

```python
offline_count = 0

for service in services:
    if service["status"] == "offline":
        offline_count += 1

return offline_count
```

The complete function should now look like this:

```python
def count_offline_services(services):
    """Count and return the number of offline services."""
    offline_count = 0

    for service in services:
        if service["status"] == "offline":
            offline_count += 1

    return offline_count
```

This loops through the services and adds one to the count whenever it finds an offline service.

Save the file and run it again.

The final line should now be:

```text
Offline services: 1
```

## Stage 6: Test It

Change the Realm Server status from `online` to `offline`.

Before running the program, work out what the new offline count should be.

Run the program. The final count should now be:

```text
Offline services: 2
```

Change the Realm Server back to `online` and run the program once more.

The final count should return to:

```text
Offline services: 1
```

## Stage 7: Commit the Fix

Run:

```bash
git status
git add .
git commit -m "Count offline game services"
git push
```

Refresh your fork on GitHub and check that both commits are visible.

## Stage 8: Why Is Git Distributed?

Open this `README.md` file and replace the line below with one or two sentences explaining why Git is described as distributed.

### Why is Git distributed?

Multiple users can work in separate branches, each working on different parts of a system, and then all merging back together to create a product that is then kept on the cloud. It does not rely on local storage, and any team member can access each module and make changes when needed.

Save the README, then run:

```bash
git status
git add .
git commit -m "Explain why Git is distributed"
git push
```

## Final Check

Before finishing, make sure that:

- Four services are displayed.
- The Auction House is offline.
- The Realm Server is online.
- The final offline count is `1`.
- You’ve answered the short Git question.
- Your changes are visible on GitHub.
- You’ve made at least three commits.

## Optional Extension

Once everything above works, update `display_services()` so that it shows a warning underneath any offline service.

For example:

```text
Auction House: offline
  WARNING: This service is unavailable
```

Test it using different service statuses and commit the extension separately.
