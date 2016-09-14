# groupmaker
Command line tool for making classroom groups.

Students are grouped by who has worked together least frequently.

## Usage

First, make a **student file** containing all of the students, one on each line.

```
Alice
Bob
Carmen
```

Then you can start making groups.

```bash
groupmaker [-n GROUP_SIZE] STUDENT_FILE
```

This will output a **group file**, with groups of students separated by a blank line.

```
Alice
Bob

Carmen
```

Those are your new groups!

If you want to make more groups taking into account historical pairings, keep around those group files and pass them in when you make new groups.
New groups pair together people who have worked with each other _least frequently_ in the past.

```bash
groupmaker [-n GROUP_SIZE] STUDENT_FILE [GROUPS_FILE [GROUPS_FILE ...]]
```

You can show a table of pairing frequencies before generating the new group with the verbose `-v` flag.
