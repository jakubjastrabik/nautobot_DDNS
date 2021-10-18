VERSION = '0.0.2'

try:
    from nautobot.extras.plugins import PluginConfig
except ImportError:
    # Dummy for when importing outside of nautobot
    class PluginConfig:
        pass


class nautobotDDNSConfig(PluginConfig):
    name = 'nautobot_ddns'
    verbose_name = 'Dynamic DNS'
    version = VERSION
    min_version = '2.8'
    max_version = '2.10.999'
    author = 'Jakub Jastrabik &&Sander Steffann'
    author_email = 'sander@steffann.nl'
    description = 'Dynamic DNS Connector for nautobot'
    base_url = 'ddns'
    required_settings = []
    default_settings = {}

    def ready(self):
        super().ready()

        from . import signals


config = nautobotDDNSConfig