from flask_nav.elements import Navbar, View, Subgroup
from transport import nav


@nav.navigation()
def navigation_bar():
    return Navbar(
        View("Home", "home"),
        View("Missions", "missions"),
        Subgroup(
            "Add",
            View("Add transportation-worker", "add_transportation_worker")
        )
    )
