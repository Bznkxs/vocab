# Readme

Vocabulary tool.

Store vocabulary in `vocab.csv` and
run:
```bash
python main.py
```



## Format

`vocab.csv` stores each word in one line in the following format:

```
word,pronunciation_hint,definition_or_comment,notable_example(s),related_expression
```

The content of each column is totally up to the user to decide. The user can leave any column empty.

For example,

```
ledge,,"the raised part of a rock, building; a narrow flat surface",window ledge,
vanity,,"conceit; something that is vain, valueless; quality of being vain; a costume case; dressing table",,conceit
```

In case the user is not familiar with `csv` format, `vocab.csv` can be opened with applications such as Excel, WPS, LibreOffice Calc, etc.