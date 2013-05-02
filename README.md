threepio
========

Minimally improved noise for python.

Pragmatic, minimal logging for python.

# Install
```bash
pip install git+git://github.com/jmatt/threepio
```

# Use

Just initialize and go.

```python
In [1]: import logging

In [2]: import threepio

In [3]: threepio.initialize(log_filename="./c3po.beep",
                            logger_name="super serial project",
                            app_logging_level=logging.DEBUG,
                            dep_logging_level=logging.WARN)
Out[3]: <logging.Logger at 0x106bc4ed0>

In [4]: from threepio import logger as c3po

In [5]: c3po.debug("BEEP!")

In [6]: c3po.info("ManBearPig Exists!")
#
# In c3po.log
# 2013-05-01 22:29:47,548 super serial project-DEBUG [<ipython-input-5-b81c1c01169e> 1] BEEP!
# 2013-05-01 22:30:01,372 super serial project-INFO [<ipython-input-6-089fe0b5bf92> 1] ManBearPig Exists!
```

Or create a custom logger and leave the global logger alone.

```python
In [1]: import logging
In [2]: import threepio
In [3]: woot_logger = threepio.initialize(logger_name="woot",
    app_logging_level=logging.DEBUG,
    dep_logging_level=logging.DEBUG,
    global_logger=False)
In [4]: woot_logger.debug("RWRAharhrhr!")
#
# In the default logging file (threepio.log)
# 2013-05-01 22:14:06,215 woot-DEBUG [<ipython-input-6-3066a630384a> 1] RWRAharhrhr!
```

***[Luke, Leia and Han start laughing hysterically; it sounds like screaming]***

**C-3PO**: Listen to them, they're dying R2! Curse my metal body, I wasn't fast enough, it's all my fault! My poor Master.

**Luke**: 3PO, we're all right! We're all right! Ha ha! Hey, open the pressure maintenance hatch on unit number... where are we? 3263827!
