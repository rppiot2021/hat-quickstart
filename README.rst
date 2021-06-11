hat-quickstart
==============

This repository contains a minimal working example that uses ``hat-core`` for
its infrastructure. The example makes use of all components that interact with
monitor and event server, others may be used optionally. To run, install the
requirements and run scripts in the ``playground/run`` directory.

This repository uses doit as its build tool, make sure to call ``doit list`` to
check available tasks. Some functions require certain tasks to be executed
before they can run properly, e.g. calling ``doit js_view`` is necessary to be
able to access the graphical interface.
