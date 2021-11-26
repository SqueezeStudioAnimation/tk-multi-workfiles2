### Squeeze - Default empty hook to resolve templates

import sgtk

HookClass = sgtk.get_hook_baseclass()


class TemplateResolver(HookClass):
    def execute(self, *args, **kwargs):
        """
        :rtype: tank.template.TemplatePath
        """
        return None
