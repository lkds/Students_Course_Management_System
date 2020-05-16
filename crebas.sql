/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/5/16 19:53:28                           */
/*==============================================================*/


drop table if exists course;

drop table if exists department;

drop table if exists sc;

drop table if exists student;

drop table if exists teacher;

/*==============================================================*/
/* Table: course                                                */
/*==============================================================*/
create table course
(
   courseID             int not null,
   teacherID            int,
   departmentID         int,
   courseName           varchar(64),
   primary key (courseID)
);

/*==============================================================*/
/* Table: department                                            */
/*==============================================================*/
create table department
(
   departmentID         int not null,
   departmentName       varchar(64),
   departmentAddress    varchar(64),
   contactInformation   varchar(64),
   primary key (departmentID)
);

/*==============================================================*/
/* Table: sc                                                    */
/*==============================================================*/
create table sc
(
   scID                 int not null,
   courseID             int,
   studentID            int,
   grades               int,
   primary key (scID)
);

/*==============================================================*/
/* Table: student                                               */
/*==============================================================*/
create table student
(
   studentID            int not null,
   departmentID         int,
   name                 varchar(64),
   studentNumber        varchar(20),
   gender               char(1),
   grade                varchar(20),
   birthday             date,
   primary key (studentID)
);

/*==============================================================*/
/* Table: teacher                                               */
/*==============================================================*/
create table teacher
(
   teacherID            int not null,
   departmentID         int,
   teacherNumber        varchar(20),
   teacherName          varchar(64),
   birthday             date,
   title                varchar(64),
   gender               char(1),
   office               varchar(64),
   homeAddress          varchar(64),
   primary key (teacherID)
);

alter table course add constraint FK_department_course foreign key (departmentID)
      references department (departmentID) on delete restrict on update restrict;

alter table course add constraint FK_teacher_course foreign key (teacherID)
      references teacher (teacherID) on delete restrict on update restrict;

alter table sc add constraint FK_course_sc foreign key (courseID)
      references course (courseID) on delete restrict on update restrict;

alter table sc add constraint FK_student_sc foreign key (studentID)
      references student (studentID) on delete restrict on update restrict;

alter table student add constraint FK_department_student foreign key (departmentID)
      references department (departmentID) on delete restrict on update restrict;

alter table teacher add constraint FK_department_teacher foreign key (departmentID)
      references department (departmentID) on delete restrict on update restrict;

