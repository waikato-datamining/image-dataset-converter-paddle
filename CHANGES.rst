Changelog
=========

0.0.3 (????-??-??)
------------------

- added `--resume_from` option to relevant readers that allows resuming the data processing
  from the first file that matches this glob expression (e.g., `*/012345.txt`)
- the `from-paddle-is` reader and `to-paddle-is` writer support custom separators for the text
  files linking image and annotation, e.g., one can use a semi-colon instead of the default
  space when file names should contain spaces as well
  (use `separator: ;` in the `train_dataset` and `val_dataset` sections)


0.0.2 (2025-03-14)
------------------

- added placeholder support: `from-paddle-ic`, `from-paddle-is`, `to-paddle-ic`, and `to-paddle-is`


0.0.1 (2025-02-11)
------------------

- initial release

