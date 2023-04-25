# Maintaining a database changelog

## Basics

- At the top of a changelog, the comment
```sql
-- liquibase formatted sql
```
must be present
- Every single change (every single line) should be prefixed with a comment of the form
```sql
-- changeset <author>:<changeset-title (what does the change do, in kebab-case)>(-<next number for the given change, i.e. 2 if it is the second line for this change>)
```
to ensure that this line is run as a separate transaction.
For example, if the author is `delvh` for the change `add teleporters`, and this is already the second line for this change, the comment should look something like

```sql
-- changeset delvh:add-teleporters-2
```
- All table and variable names put an `_` before a beginning uppercase letter and afterwards the name is lowercase. This means for example that `methodHTTP` would be referenced as `method_http` in the database
- All artificial table names are created as `<table_name>_<variable_name>`, so i.e. the fictional `BookDTO#referencedCourse` variable would be transformed into a table with name `book_dto_referenced_course` (needed for the relation tables as outlined below)
- Now, you're ready to implement the actual changes

## Adding a new table

To create a completely new table, use the syntax
```sql
CREATE TABLE "<table name as described above>" (<variable pairs, comma-separated>, CONSTRAINT "<the table name as earlier>_pkey" PRIMARY KEY ("id")); -- Regarding the last "id": or whatever column else you use as your ID column
```
where each `variable pair` follows the schema
```sql
"<variable name>" <variable type> <remaining conditions, i.e. NOT NULL>
```
For example,
```sql
CREATE TABLE "book" ("id" UUID NOT NULL, "description" VARCHAR(255), "index" INTEGER NOT NULL, "text" VARCHAR(1000000), "area_id" UUID, "course_id" INTEGER, CONSTRAINT "book_pkey" PRIMARY KEY ("id"));
```
is the correct snippet for the corresponding Java type
```java
@Entity
//@Table(uniqueConstraints = { @UniqueConstraint(columnNames = { "index", "area_id", "course_id" }) }) // <- That will be explained below in the section "Adding unique constraints"
@Data
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
public class Book {

    @Id
    @GeneratedValue(generator = "uuid")
    UUID id;

    int index;

    @Column(length = 1000000)
    String text;

    @Nullable
    String description;

    //@ManyToOne
    //Course course; // <- See section "Relations" below

    //@ManyToOne
    //Area area; // <- See section "Relations" below
}
```

## Relations

### One-to-one

See [Many-to-One](#many-to-one), except that the column

### One-to-many

If you have a `one-to-many` relation, you need an extra table like the following:
```sql
CREATE TABLE "<table name as described above for the variable declaring the one-to-many relation>" ("<lowercase(class)>_id" <ID type of the declaring class> NOT NULL, "<lowercase(variable)_lowercase(name)>_id" <ID type of the other class> NOT NULL, CONSTRAINT "<table name as before>_pkey" PRIMARY KEY ("<first variable in this table>", "<second variable in this table>"));
```
So, for example
```sql
CREATE TABLE "area_minigame_tasks" ("area_id" UUID NOT NULL, "minigame_tasks_id" UUID NOT NULL, CONSTRAINT "area_minigame_tasks_pkey" PRIMARY KEY ("area_id", "minigame_tasks_id"));
```
Creates a helper table for the snippet
```java
@Entity
class Area {
	@Id(generator="uuid")
	UUID id;

	@OneToMany
	Set<MinigameTask> minigameTasks;
}
```

### Many-to-one

For a `many-to-one` relation, you need to do two things:
Firstly, your table declaring the `many-to-one` relation needs a column `<referenced variable>_id <ID type of the referenced table>`.
Secondly, you need to create a foreign key by executing
```sql
ALTER TABLE "<table name of the class declaring the many-to-one relation>" ADD CONSTRAINT "fk<random alphanumeric string of length 25, result must simply be globally unique in your db>" FOREIGN KEY ("<referenced variable>_id") REFERENCES "<table name of the related class>" ("<ID column of the referenced table>") ON UPDATE NO ACTION ON DELETE NO ACTION; -- regarding the "ON" part: or whatever else you entered as CASCADE
```
To give you an example, given the following snippet
```java
@Entity
class Area {
	@Id
	UUID id;

	@ManyToOne
	Course course;
}
…
@Entity
class Course {
	@Id
	int id;
}
```
you need to record both the following statements:
```sql
-- changeset delvh:add-courses-to-areas-1
CREATE TABLE "area" ("id" UUID, "course_id" INTEGER, "world_id" UUID, CONSTRAINT "area_pkey" PRIMARY KEY ("id")); -- alternatively an ALTER TABLE if the table exists already

-- changeset delvh:add-courses-to-areas-2
ALTER TABLE "area" ADD CONSTRAINT "fkke3rmfk70r7ot54sy24vw442q" FOREIGN KEY ("course_id") REFERENCES "course" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION;
```

### Many-to-many

See One-to-many. <!-- TODO: really? -->

## Constraints

### Indices

To add an index to a table, add the following to your changelog:
```sql
CREATE INDEX <lowercased unique name that indicates what this index is used for> ON <tablename> (<column names comma separated>)
```
so, for example:
```sql
CREATE INDEX index_book_content_creator ON book ("content", "creator_id")
```

### Unique constraints

To add a unique constraint to a table, add the following to your changelog:
```sql
ALTER TABLE "<table with the unique constraint>" ADD CONSTRAINT "uk<random alphanumeric string of length 25, result must simply be globally unique in your db>" UNIQUE (<column names comma separated>);
```
so, for example:
```sql
ALTER TABLE "course" ADD CONSTRAINT "uk820tkd4yvetwbn59037xp1ix0" UNIQUE ("course_name", "semester");
```

