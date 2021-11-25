### Squeeze - Default empty hook to resolve work templates

import sgtk

HookClass = sgtk.get_hook_baseclass()


class TemplateResolver(HookClass):
    def execute(self, *args, **kwargs):
        return None
