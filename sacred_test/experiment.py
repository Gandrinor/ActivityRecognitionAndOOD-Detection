from sacred import Experiment
import os

ex = Experiment('hello_config')

@ex.config
def my_config():
    dummy = 0
    change = False

@ex.capture
def log_sth(_log, change: bool):
    if change:
        _log.info('info: {}'.format(change))
        _log.warning('warning: {}'.format(change))


@ex.capture
def log_dir(_log):
    _log.info('where am i?: {}'.format(os.getcwd()))
    _log.info('home exists?: {}'.format(os.path.exists("/home/sbartkow/code/")))
    _log.info('data exists?: {}'.format(os.path.exists("/data/sbartkow/")))



# all code above automain to be defined

@ex.automain
def my_main(_run, dummy, change):

    if _run is not None:
        log_dir()
        for i in range(50):
            if change:
                dummy += i
            else:
                dummy -= i
            _run.log_scalar("counter", dummy, i * 2)
            if i % 5 == 0:
                change = not change
                log_sth(change=change)