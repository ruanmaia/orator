# -*- coding: utf-8 -*-


class Connector(object):

    RESERVED_KEYWORDS = [
        'log_queries', 'driver', 'prefix', 'name'
    ]

    def get_api(self):
        raise NotImplementedError()

    def get_config(self, config):
        default_config = self.get_default_config()
        config = {x: config[x] for x in config if x not in self.RESERVED_KEYWORDS}

        default_config.update(config)

        return default_config

    def get_default_config(self):
        return {}

    def connect(self, config):
        return self.get_api().connect(**self.get_config(config))
