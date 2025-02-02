from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register

PLUGIN_NAME = 'astrbot_plugin_wo'
PLUGIN_AUTHOR = 'wooyo20'
PLUGIN_DESC = '一个简单插件'
PLUGIN_VERSION = '1.0.0'


@register(PLUGIN_NAME, PLUGIN_AUTHOR, PLUGIN_DESC, PLUGIN_VERSION)
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("wo")
    async def helloworld(self, event: AstrMessageEvent):
        user_name = event.get_sender_name()
        yield event.plain_result(f"Hello, {user_name}!")  # 发送一条纯文本消息
