"""Provides functions that are utilized by the command line interface.

In particular, the examples are exposed to the command line interface
(defined in `softlearning.scripts.console_scripts`) through the
`get_trainable_class`, `get_variant_spec`, and `get_parser` functions.
"""


def get_trainable_class(*args, **kwargs):
    from .main import ExperimentRunner
    return ExperimentRunner


def get_variant_spec(command_line_args, *args, **kwargs):
    # command_line_args 是 parser 解析出的结果加部分默认值
    from .variants import get_variant_spec
    # 实例对象的配置文件的生成
    variant_spec = get_variant_spec(command_line_args, *args, **kwargs)
    return variant_spec


def get_parser():
    from examples.utils import get_parser
    parser = get_parser()  # 最外层是 算法 环境 相关的设置
    #  包含了 parser = add_ray_init_args(parser)
    #  和 parser = add_ray_tune_args(parser)
    return parser
