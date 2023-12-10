Dragonfly (modified)
====================

This is a fork of the Dragonfly project, a speech recognition framework for Python. 
The originating project source can be found at 
[dictation-toolbox/dragonfly](https://github.com/dictation-toolbox/dragonfly).

This fork is intended to accommodate specific modifications required for applications
built by [JWebmeister](https://github.com/jwebmeister). 
Modifications include:

- Re-enabled notifications to `KaldiRecObsManager` within the Kaldi engine backend.
- Added `notify_partial_recognition` and related to engine and recobs, specifically for the Kaldi engine. 
- Added `listen_key` (keyboard or mouse) with hold or toggle modes to Kaldi engine. Hold or toggle modes include:
    - `0: Hold`; listen only while key is pressed, release key to finish utterance.
    - `1: Toggle`; listen while on, press key to toggle on or off, must toggle off to finish utterance.
    - `2: Global toggle`; always listening while on, press key to toggle on or off, finishes utterance based on Voice Activity Detector (VAD).
    - `-1: Priority hold`; always listen for *only* priority grammar (and all recobs), listen for all grammar while key is pressed, release key to finish utterance and also deactivate non-priority grammar.


These modifications are intended to:

- *decrease the delay* between speech and the execution of matching rules callback functions.
    - e.g. "Freeze this is the police!", match on recognition of the word "Freeze", and execute a function before the rest of the sentence has been fully spoken.
- *reduce false positive recognitions*.
    - e.g. change listening mode to on or off with a key press.

Installation
------------------------------------------
First, clone this repo into a folder, e.g. `dragonfly/`.

Run the following command (or similar) while in the dragonfly project folder:

    pip install -e .

To build the dragonfly python package, run these commands in the projects root directory.

    pip install build  
    python -m build


Further information
----------------------------------------------------------------------------

For further information on how to use Dragonfly:

- source code for this fork at [jwebmeister/dragonfly](https://github.com/jwebmeister/dragonfly).
- documentation is available online at [Read the Docs](http://dragonfly.readthedocs.org/en/latest/).
- the originating project source can be found at [dictation-toolbox/dragonfly](https://github.com/dictation-toolbox/dragonfly).
