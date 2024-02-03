from sufficient.frames import *


class App:
    name = "GM Universe"
    description = "A boilerplate for creating frame apps"
    image = "{uri}/static/home.svg"
    uri = "{uri}"
    start = "PageHome"


class PageHome:
    def view(self, action: Action, result: ActionResult):
        return SvgFile("home.svg")

    def btn_normal_button(self, action: Action):
        return "PageNext"

    def goto_redirect_button(self, action: Action):
        return "https://github.com/briceyan/frame-app-boilerplate"

    def input_input_text(self, action: Action):
        # wip
        pass


class PageNext:
    def view(self, action: Action, result: ActionResult):
        return SvgTemplate("foo.svg", title="PageNext", content="hello")

    def btn_prev(self, action: Action):
        return "PageHome"

    def btn_refresh(self, action: Action):
        return "PageNext"
