game_services = [
    {"name": "Login Service", "status": "online"},
    {"name": "Realm Server", "status": "online"},
    {"name": "Auction House", "status": "offline"},
    {"name": "In-game Mail", "status": "online"}
]


def display_services(services):
    """Display the name and status of every game service."""
    for service in services:
        print(f"{service['name']}: {service['status']}")


def count_offline_services(services):
    """Count and return the number of offline services."""
    # TODO: Replace the line below by following Stage 6 in README.md.
    return 0


print("LAUNCH NIGHT SERVICE MONITOR")
print("=" * 28)

display_services(game_services)

offline_services = count_offline_services(game_services)
print(f"\nOffline services: {offline_services}")
