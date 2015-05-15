BEGIN;
CREATE TABLE "historynet_login" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_name" varchar(50) NOT NULL,
    "password" varchar(50) NOT NULL,
    "email" varchar(100) NOT NULL,
    "level" smallint NOT NULL,
    "estado" smallint NOT NULL,
    "last_login" datetime NOT NULL
)
;
CREATE TABLE "historynet_usuario" (
    "login_id" integer NOT NULL PRIMARY KEY REFERENCES "historynet_login" ("id"),
    "nombre" varchar(150) NOT NULL,
    "apellido" varchar(150) NOT NULL,
    "pais" varchar(15) NOT NULL,
    "sexo" varchar(1) NOT NULL
)
;
CREATE TABLE "historynet_lugar" (
    "id" integer NOT NULL PRIMARY KEY,
    "nombre" varchar(150) NOT NULL,
    "direccion" varchar(1024) NOT NULL,
    "informacion_primaria" varchar(1024) NOT NULL,
    "longitud" real NOT NULL,
    "latitud" real NOT NULL,
    "fecha" datetime NOT NULL,
    "valoracion" real NOT NULL,
    "denuncia" integer NOT NULL,
    "estado" smallint NOT NULL
)
;
CREATE TABLE "historynet_informacion_adicional" (
    "id" integer NOT NULL PRIMARY KEY,
    "lugar_id_id" integer NOT NULL REFERENCES "historynet_lugar" ("id"),
    "mensaje" varchar(1024) NOT NULL,
    "fecha" datetime NOT NULL,
    "denuncia" integer NOT NULL,
    "estado" smallint NOT NULL
)
;
CREATE TABLE "historynet_comentario" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id_id" integer NOT NULL REFERENCES "historynet_usuario" ("login_id"),
    "lugar_id_id" integer NOT NULL REFERENCES "historynet_lugar" ("id"),
    "mensaje" varchar(1024) NOT NULL,
    "fecha" datetime NOT NULL,
    "valoracion" real NOT NULL,
    "denuncia" integer NOT NULL,
    "estado" smallint NOT NULL
)
;
CREATE TABLE "historynet_lugares_favoritos_user_id" (
    "id" integer NOT NULL PRIMARY KEY,
    "lugares_favoritos_id" integer NOT NULL,
    "usuario_id" integer NOT NULL REFERENCES "historynet_usuario" ("login_id"),
    UNIQUE ("lugares_favoritos_id", "usuario_id")
)
;
CREATE TABLE "historynet_lugares_favoritos_lugar_id" (
    "id" integer NOT NULL PRIMARY KEY,
    "lugares_favoritos_id" integer NOT NULL,
    "lugar_id" integer NOT NULL REFERENCES "historynet_lugar" ("id"),
    UNIQUE ("lugares_favoritos_id", "lugar_id")
)
;
CREATE TABLE "historynet_lugares_favoritos" (
    "id" integer NOT NULL PRIMARY KEY
)
;
CREATE TABLE "historynet_valoraciones_comentarios" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id_id" integer NOT NULL UNIQUE REFERENCES "historynet_usuario" ("login_id"),
    "comentario_id_id" integer NOT NULL UNIQUE REFERENCES "historynet_comentario" ("id"),
    "valoracion" integer NOT NULL
)
;
CREATE TABLE "historynet_valoraciones_info_adicional" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id_id" integer NOT NULL UNIQUE REFERENCES "historynet_usuario" ("login_id"),
    "info_adicional_id_id" integer NOT NULL UNIQUE REFERENCES "historynet_informacion_adicional" ("id"),
    "valoracion" integer NOT NULL
)
;
CREATE TABLE "historynet_valoraciones_lugar" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id_id" integer NOT NULL UNIQUE REFERENCES "historynet_usuario" ("login_id"),
    "lugar_id_id" integer NOT NULL UNIQUE REFERENCES "historynet_lugar" ("id"),
    "valoracion" integer NOT NULL
)
;

COMMIT;
