create table if not exists gremistas (
	id serial primary key,
	nome varchar(100) not null,
	matricula varchar(20) not null unique,
	cargo varchar(50)
)

create table if not exists categorias (
	id serial primary key,
	nome_categoria varchar(50) not null unique
)

create table if not exists locais (
	id serial primary key,
	nome_local varchar(100) not null,
	bloco varchar(10) not null
)

create table if not exists itens (
	id serial primary key,
	descricao text not null,
	data_registro date default current_date,
	status varchar(20) default 'perdido',
	dono_recuperou varchar(100) null,
	
	categoria_id int,
	local_id int,
	usuario_recebeu_id int,
	gremista_entregou_id int,

	foreign key (categoria_id) references categorias(id) on delete set NULL,
	foreign key (local_id) references locais(id) on delete set NULL,
	foreign key (usuario_recebeu_id) references gremistas(id) on delete set NULL,
	foreign key (gremista_entregou_id) references gremistas(id) on delete set NULL
)

INSERT INTO gremistas (nome, matricula, cargo) VALUES
	('Grazielly Souza', '2024-109-401-00123', 'Coordenadora Geral'),
	('Yonara Gomes', '2024-401-34', 'Voluntária'),
	('Alice Mateus', '2024-109-116-00143', 'SEC Mulheres'),
	('Lara Maryana', '2024-109-116-00129', 'Coordenadora Geral'),
	('Bruno Sena', '2024-109-401-00143', 'Secretário-Geral'),
	('Pedro Heitor', '2024-109-401-0080', 'Secretário-Geral');

INSERT INTO categorias (nome_categoria) VALUES
	('Eletrônico'),
	('Material Escolar'),
	('Vestuário'),
	('Calçado'),
	('Acessório'),
	('Documento'),
	('Garrafa'),
	('Outros');

INSERT INTO locais (nome_local, bloco) VALUES
	('Sala de Aula 01', 'Principal'),
	('Sala de Aula 02', 'Principal'),
	('Sala de Aula 03', 'Principal'),
	('Sala de Aula 04', 'Principal'),
	('Sala de Aula 05', 'Anexo'),
	('Sala de Aula 06', 'Anexo'),
	('Biblioteca', 'Principal'),
	('Pátio Central', 'Principal'),
	('Quadra Poliesportiva', 'Anexo'),
	('Cantina', 'Principal');

INSERT INTO itens (
    descricao,
    data_registro,
    status,
    dono_recuperou,
    categoria_id,
    local_id,
    usuario_recebeu_id,
    gremista_entregou_id) VALUES
	('iPhone 15 Preto', '2026-05-20', 'perdido', NULL, 1, 8, 1, NULL),
	('Fone Bluetooth JBL Branco', '2026-05-21', 'guardado', NULL, 1, 7, 2, 4),
	('Caderno de Matemática capa azul', '2026-05-21', 'entregue', 'Maria Eduarda', 2, 1, 1, 5),
	('Moletom cinza tamanho M', '2026-05-22', 'guardado', NULL, 3, 9, 3, 2),
	('Casaco preto com capuz', '2026-05-22', 'perdido', NULL, 3, 10, 4, NULL),
	('Tênis Nike branco nº 39', '2026-05-23', 'guardado', NULL, 4, 8, 2, 6),
	('Carteira estudantil', '2026-05-23', 'entregue', 'Pedro Henrique', 6, 2, 5, 1),
	('Pulseira prata', '2026-05-24', 'guardado', NULL, 5, 7, 6, 3),
	('Garrafa térmica azul', '2026-05-24', 'perdido', NULL, 7, 10, 1, NULL),
	('Tablet Samsung Galaxy Tab', '2026-05-25', 'guardado', NULL, 1, 3, 4, 5),
	('Óculos de grau preto', '2026-05-25', 'entregue', 'João Vitor', 5, 8, 2, 4);