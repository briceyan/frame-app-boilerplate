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
        result = ActionResult(title="PageNext", content=action.input_text)
        return "PageNext", result

    def goto_redirect_button(self, action: Action):
        return "https://github.com/briceyan/frame-app-boilerplate"

    def input_input_text(self):
        # wip
        pass


class PageNext:
    def view(self, action: Action, result: ActionResult):
        args = ActionResult(title="PageNext", content="hello world")
        return SvgTemplate("foo.svg", args)

    def btn_prev(self, action: Action):
        return "PageHome"

    def btn_refresh(self, action: Action):
        return "PageNext"
