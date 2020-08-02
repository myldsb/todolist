-- create user table.
create table if not exists user (id integer primary key autoincrement,
                                name varchar(20) not null unique ,
                                passwd varchar(36) not null,
                                email varchar(255) not null unique default "",
                                isDeleted bool not null default FALSE
                                );

-- create todolist table.
create table if not exists todolist (id integer primary key autoincrement,
                                    title varchar(255) not null,
                                    body varchar(255) not null,
                                    time char(16) not null,
                                    send_email bool not null default FALSE,
                                    state bool not null default FALSE,
                                    remark varchar(255) not null default "",
                                    owner integer,
                                    foreign key(owner) references user(id) on delete cascade on update cascade
                                    );

-- insert
insert or replace into user values(1,
                                "admin",
                                "21232f297a57a5a743894a0e4a801fc3", -- md5("admin")
                                "xxxx@163.com",
                                null
                                );

insert or replace into todolist values(null,
                                "编程",
                                "不敲代码就浑身瘙痒",
                                "2020-02-20 08:00",
                                null,
                                null,
                                null,
                                1
                                );
