create table Session (
    Id integer not null primary key autoincrement,
    GuildId text not null,
    ChannelId text not null,
    GameMasterUserId text not null,
    Finished boolean not null default False
);

create table SpellCast (
    Id integer not null primary key autoincrement,
    Effect text not null,
    Hidden boolean not null default True,
    UserId text not null,
    SessionId integer not null,
    foreign key(SessionId) references Session(Id)
);

create table StoredSpellCast (
    Id integer not null primary key autoincrement,
    Effect text not null,
    Hidden boolean not null default True,
    UserId text not null,
    SessionId integer not null,
    foreign key(SessionId) references Session(Id)
);

-- insert into Assets(GuildId, Id, AssetFilename)
-- values 
--     (968213148786118656,'16209f54-2965-4410-8884-7bc774654507', '1.jpg'),
--     (968213148786118656,'fce775cd-271f-4d2e-98fa-4498dfde0094', '2.jpg'),
--     (968213148786118656,'16209f54-2965-4410-8884-7bc774654502', '3.jpg');

-- insert into AssetAnswers(AssetId, AssetAnswer)
-- values
--     ('16209f54-2965-4410-8884-7bc774654507', 'mountain'),
--     ('16209f54-2965-4410-8884-7bc774654507', 'mist'),
--     ('fce775cd-271f-4d2e-98fa-4498dfde0094', 'girl'),
--     ('fce775cd-271f-4d2e-98fa-4498dfde0094', 'sleep'),
--     ('16209f54-2965-4410-8884-7bc774654507', 'nebula'),
--     ('16209f54-2965-4410-8884-7bc774654502', 'bubble');
