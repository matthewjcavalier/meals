use meal_maker;

create table ingredients
(
  name          varchar(255) not null,
  store_section varchar(255) null,
  constraint ingredients_name_uindex
    unique (name)
);

alter table ingredients
  add primary key (name);

create table recipe
(
  id   int auto_increment
    primary key,
  name varchar(255) not null
);

create table recipe_ingredients
(
  amount     varchar(255) not null,
  name       varchar(255) not null,
  recipe_id int          null,
  constraint recipe_ingredients_ibfk_1
    foreign key (recipe_id) references recipe (id)
);

create index recipe_id
  on recipe_ingredients (recipe_id);

create table recipe_steps
(
  step_number int           not null,
  text        varchar(1000) not null,
  recipe_id   int           null,
  constraint recipe_steps_ibfk_1
    foreign key (recipe_id) references recipe (id)
);

create index recipe_id
  on recipe_steps (recipe_id);

insert into meal_maker.recipe (name) values ("Ham Sandwich");

insert into meal_maker.recipe_ingredients (amount, name, recipe_id) values ("4 slices", "pickle",	1);
insert into meal_maker.recipe_ingredients (amount, name, recipe_id) values ("3 slices", "ham",	1);
insert into meal_maker.recipe_ingredients (amount, name, recipe_id) values ("2 slices", "cheese",	1);
insert into meal_maker.recipe_ingredients (amount, name, recipe_id) values ("2 slices", "bread",	1);

insert into meal_maker.recipe_steps (step_number, text, recipe_id) values(1,	"Place down 1 slice of bread",	1);
insert into meal_maker.recipe_steps (step_number, text, recipe_id) values(2,	"Add the cheese",	1);
insert into meal_maker.recipe_steps (step_number, text, recipe_id) values(3,	"Add the pickles",	1);
insert into meal_maker.recipe_steps (step_number, text, recipe_id) values(4,	"Add the Ham",	1);
insert into meal_maker.recipe_steps (step_number, text, recipe_id) values(5,	"Add the 2nd slice of bread",	1);
