-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION pg_database_owner;

-- DROP SEQUENCE public.categorias_id_seq;

CREATE SEQUENCE public.categorias_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.gremistas_id_seq;

CREATE SEQUENCE public.gremistas_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.itens_id_seq;

CREATE SEQUENCE public.itens_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.locais_id_seq;

CREATE SEQUENCE public.locais_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;-- public.categorias definição

-- Drop table

-- DROP TABLE public.categorias;

CREATE TABLE public.categorias (
	id serial4 NOT NULL,
	nome_categoria varchar(50) NOT NULL,
	CONSTRAINT categorias_pkey PRIMARY KEY (id)
);


-- public.gremistas definição

-- Drop table

-- DROP TABLE public.gremistas;

CREATE TABLE public.gremistas (
	id serial4 NOT NULL,
	nome varchar(100) NOT NULL,
	matricula varchar(20) NOT NULL,
	cargo varchar(50) NOT NULL,
	CONSTRAINT gremistas_pkey PRIMARY KEY (id)
);


-- public.locais definição

-- Drop table

-- DROP TABLE public.locais;

CREATE TABLE public.locais (
	id serial4 NOT NULL,
	nome_local varchar(100) NOT NULL,
	bloco varchar(10) NOT NULL,
	CONSTRAINT locais_pkey PRIMARY KEY (id)
);


-- public.itens definição

-- Drop table

-- DROP TABLE public.itens;

CREATE TABLE public.itens (
	id serial4 NOT NULL,
	descricao text NOT NULL,
	data_registro date NULL,
	status varchar(20) NULL,
	dono_recuperou varchar(100) NULL,
	categoria_id int4 NOT NULL,
	local_id int4 NOT NULL,
	gremista_recebeu_id int4 NOT NULL,
	gremista_entregou_id int4 NOT NULL,
	CONSTRAINT itens_pkey PRIMARY KEY (id),
	CONSTRAINT fk_recebeu FOREIGN KEY (gremista_recebeu_id) REFERENCES public.gremistas(id)
);

-- Drop table

-- DROP TABLE public.categorias;

CREATE TABLE public.categorias (
	id serial4 NOT NULL,
	nome_categoria varchar(50) NOT NULL,
	CONSTRAINT categorias_pkey PRIMARY KEY (id)
);

-- Drop table

-- DROP TABLE public.gremistas;

CREATE TABLE public.gremistas (
	id serial4 NOT NULL,
	nome varchar(100) NOT NULL,
	matricula varchar(20) NOT NULL,
	cargo varchar(50) NOT NULL,
	CONSTRAINT gremistas_pkey PRIMARY KEY (id)
);

-- Drop table

-- DROP TABLE public.itens;

CREATE TABLE public.itens (
	id serial4 NOT NULL,
	descricao text NOT NULL,
	data_registro date NULL,
	status varchar(20) NULL,
	dono_recuperou varchar(100) NULL,
	categoria_id int4 NOT NULL,
	local_id int4 NOT NULL,
	gremista_recebeu_id int4 NOT NULL,
	gremista_entregou_id int4 NOT NULL,
	CONSTRAINT itens_pkey PRIMARY KEY (id),
	CONSTRAINT fk_recebeu FOREIGN KEY (gremista_recebeu_id) REFERENCES public.gremistas(id)
);

-- Drop table

-- DROP TABLE public.locais;

CREATE TABLE public.locais (
	id serial4 NOT NULL,
	nome_local varchar(100) NOT NULL,
	bloco varchar(10) NOT NULL,
	CONSTRAINT locais_pkey PRIMARY KEY (id)
);