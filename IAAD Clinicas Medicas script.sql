#drop schema Clinica_IAAD;
create schema Clinica_IAAD;
use Clinica_IAAD;

create table Clinica (
CodCli CHAR(7) NOT NULL,
NomeCli VARCHAR(40) NOT NULL,
Endereco VARCHAR(50),
Telefone CHAR(16),
Email VARCHAR(40),
PRIMARY KEY (CodCli)
);

create table Medico (
CodMed CHAR(7),
NomeMed VARCHAR(40) NOT  NULL,
Genero CHAR(1),
Telefone CHAR(16),
Email VARCHAR(40),
CodEspec CHAR(7),
PRIMARY KEY (CodMed),
UNIQUE (Email)
);

create table Paciente (
CpfPaciente CHAR(11),
NomePac VARCHAR(40) NOT NULL,
DataNascimento DATE NOT NULL,
Genero CHAR(1),
Telefone CHAR(16),
Email VARCHAR(40),
PRIMARY KEY (CpfPaciente),
UNIQUE (Email)
);

create table ClinicaMedico (
CodCLi CHAR(7) NOT NULL,
CodMEd CHAR(7) NOT NULL,
DataIngresso DATE NOT NULL,
CargaHorariaSemanal DECIMAL(3,1) DEFAULT 20.0,
PRIMARY KEY (CodCli, CodMed)
);


create table AgendaConsulta (
CodCli CHAR(7) NOT NULL,
CodMEd CHAR(7) NOT NULL,
CpfPaciente CHAR(11) NOT NULL,
Data_Hora DATETIME NOT NULL,
PRIMARY KEY (CodCli, CodMed, CpfPaciente, Data_Hora)
);

create table Especialidade (
CodEspec CHAR(7),
NomeEspec VARCHAR(40),
Descricao TEXT NOT NULL,
PRIMARY KEY (CodEspec)
);


INSERT INTO Medico (CodMed, NomeMed, Genero, Telefone, Email, CodEspec) VALUES
('MED001', 'Fernanda Silva', 'F', '(11) 1234-5678', 'fernanda.silva@example.com', 'ESP001'),
('MED002', 'João Santos', 'M', '(22) 9876-5432', 'joao.santos@example.com', 'ESP002'),
('MED003', 'Maria Oliveira', 'F', '(33) 4567-8901', 'maria.oliveira@example.com', 'ESP003'),
('MED004', 'Pedro Souza', 'M', '(44) 5678-9012', 'pedro.souza@example.com', 'ESP004'),
('MED005', 'Julia Rodrigues', 'F', '(55) 6789-0123', 'julia.rodrigues@example.com', 'ESP005'),
('MED006', 'Lucas Santos', 'M', '(11) 2345-6789', 'lucas.santos@example.com', 'ESP001'),
('MED007', 'Gabriela Almeida', 'F', '(22) 8765-4321', 'gabriela.almeida@example.com', 'ESP002'),
('MED008', 'Ricardo Lima', 'M', '(33) 7890-1234', 'ricardo.lima@example.com', 'ESP003'),
('MED009', 'Ana Paula Costa', 'F', '(44) 3456-7890', 'ana.costa@example.com', 'ESP004'),
('MED010', 'Bruno Castro', 'M', '(55) 9012-3456', 'bruno.castro@example.com', 'ESP005'),
('MED011', 'Juliana Santos', 'F', '(11) 3456-7890', 'juliana.santos@example.com', 'ESP001'),
('MED012', 'Leandro Silva', 'M', '(22) 9012-3456', 'leandro.silva@example.com', 'ESP002'),
('MED013', 'Luana Ferreira', 'F', '(33) 2345-6789', 'luana.ferreira@example.com', 'ESP003'),
('MED014', 'Mariana Oliveira', 'F', '(44) 8765-4321', 'mariana.oliveira@example.com', 'ESP004'),
('MED015', 'Matheus Souza', 'M', '(55) 7890-1234', 'matheus.souza@example.com', 'ESP005'),
('MED016', 'Natalia Santos', 'F', '(11) 6789-0123', 'natalia.santos@example.com', 'ESP001'),
('MED017', 'Paulo Oliveira', 'M', '(22) 3456-7890', 'paulo.oliveira@example.com', 'ESP002'),
('MED018', 'Raquel Lima', 'F', '(33) 9012-3456', 'raquel.lima@example.com', 'ESP003'),
('MED019', 'Rodrigo Castro', 'M', '(44) 2345-6789', 'rodrigo.castro@example.com', 'ESP004'),
('MED020', 'Sara Costa', 'F', '(55) 8765-4321', 'sara.costa@example.com', 'ESP005');


INSERT INTO Clinica (CodCli, NomeCli, Endereco, Telefone, Email) VALUES
('9999999', 'DEFAULT', 'N/A', 'N/A', 'N/A'),
('CLIN001', 'Clinica ABC', 'Rua A, 123', '(11) 1234-5678', 'clinicaabc@example.com'),
('CLIN002', 'Clinica XYZ', 'Avenida B, 456', '(22) 9876-5432', 'clinicaxyz@example.com'),
('CLIN003', 'Clinica 123', 'Rua C, 789', '(33) 4567-8901', 'clinica123@example.com'),
('CLIN004', 'Clinica Saude', 'Avenida D, 234', '(44) 5678-9012', 'clinicasaude@example.com'),
('CLIN005', 'Clinica Bem-Estar', 'Rua E, 567', '(55) 6789-0123', 'clinicabemestar@example.com');


INSERT INTO Paciente (CpfPaciente, NomePac, DataNascimento, Genero, Telefone, Email) VALUES
('12345678901', 'João da Silva', '1990-05-15', 'M', '(11) 1111-1111', 'joao.silva@email.com'),
('23456789012', 'Maria Santos', '1985-02-28', 'F', '(22) 2222-2222', 'maria.santos@email.com'),
('34567890123', 'José Oliveira', '1978-10-12', 'M', '(33) 3333-3333', 'jose.oliveira@email.com'),
('45678901234', 'Ana Paula', '2000-07-01', 'F', '(44) 4444-4444', 'anapaula@gmail.com'),
('56789012345', 'Lucas Fernandes', '1995-04-18', 'M', '(55) 5555-5555', 'lucasfernandes@hotmail.com'),
('67890123456', 'Amanda Castro', '1988-12-05', 'F', '(66) 6666-6666', 'amandacastro@yahoo.com'),
('78901234567', 'Pedro Silva', '1976-09-20', 'M', '(77) 7777-7777', 'pedrosilva@gmail.com'),
('89012345678', 'Mariana Lima', '1998-06-03', 'F', '(88) 8888-8888', 'mariana.lima@hotmail.com'),
('90123456789', 'Fernando Souza', '1983-03-22', 'M', '(99) 9999-9999', 'fernandosouza@gmail.com'),
('01234567890', 'Gabriela Martins', '2001-11-08', 'F', '(12) 1212-1212', 'gabrielamartins@yahoo.com');


INSERT INTO AgendaConsulta (CodCli, CodMEd, CpfPaciente, Data_Hora)
VALUES
('CLIN001', 'MED001', '12345678901', '2023-04-15 10:00:00'),
('CLIN002', 'MED003', '23456789012', '2023-04-16 11:30:00'),
('CLIN003', 'MED005', '34567890123', '2023-04-17 14:00:00'),
('CLIN004', 'MED007', '45678901234', '2023-04-18 15:30:00'),
('CLIN005', 'MED009', '56789012345', '2023-04-19 16:00:00'),
('CLIN001', 'MED002', '67890123456', '2023-04-20 10:30:00'),
('CLIN002', 'MED004', '78901234567', '2023-04-21 11:00:00'),
('CLIN003', 'MED006', '89012345678', '2023-04-22 14:30:00'),
('CLIN004', 'MED007', '90123456789', '2023-04-23 15:00:00'),
('CLIN005', 'MED009', '01234567890', '2023-04-24 16:30:00');


INSERT INTO ClinicaMedico (CodCli, CodMed, DataIngresso, CargaHorariaSemanal) VALUES
('CLIN001', 'MED001', '2021-01-01', 40.0),
('CLIN001', 'MED002', '2021-02-01', 20.0),
('CLIN002', 'MED003', '2021-03-01', 30.0),
('CLIN002', 'MED004', '2021-04-01', 20.0),
('CLIN003', 'MED005', '2021-05-01', 40.0),
('CLIN003', 'MED006', '2021-06-01', 20.0),
('CLIN004', 'MED007', '2021-07-01', 30.0),
('CLIN004', 'MED008', '2021-08-01', 20.0),
('CLIN005', 'MED009', '2021-09-01', 40.0),
('CLIN005', 'MED010', '2021-10-01', 20.0),
('CLIN001', 'MED011', '2021-01-01', 30.0),
('CLIN001', 'MED012', '2021-02-01', 25.0),
('CLIN002', 'MED013', '2021-03-01', 20.0),
('CLIN002', 'MED014', '2021-04-01', 30.0),
('CLIN003', 'MED015', '2021-05-01', 25.0),
('CLIN003', 'MED016', '2021-06-01', 30.0),
('CLIN004', 'MED017', '2021-07-01', 20.0),
('CLIN004', 'MED018', '2021-08-01', 25.0),
('CLIN005', 'MED019', '2021-09-01', 30.0),
('CLIN005', 'MED020', '2021-10-01', 25.0);


INSERT INTO Especialidade (CodEspec, NomeEspec, Descricao)
VALUES
('ESP001', 'Cardiologia', 'Especialidade médica que se ocupa do diagnóstico e tratamento das doenças do coração e do sistema cardiovascular.'),
('ESP002', 'Pediatria', 'Especialidade médica que se dedica à assistência à criança e ao adolescente, nos seus diversos aspectos, sejam eles preventivos ou curativos.'),
('ESP003', 'Ginecologia e Obstetrícia', 'Especialidade médica que trata do sistema reprodutor feminino, útero, vagina e ovários, bem como a gestação.'),
('ESP004', 'Dermatologia', 'Especialidade médica que se ocupa do diagnóstico e tratamento clínico-cirúrgico das doenças da pele.'),
('ESP005', 'Ortopedia', 'Especialidade médica que cuida das doenças e deformidades dos ossos, músculos, ligamentos e articulações.');




alter table Medico ADD FOREIGN KEY(CodEspec) REFERENCES Especialidade(CodEspec) ON DELETE CASCADE ON UPDATE CASCADE;

alter table ClinicaMedico ADD FOREIGN KEY(CodCli) REFERENCES Clinica(CodCli);

alter table ClinicaMedico ADD FOREIGN KEY(CodMed) REFERENCES Medico(CodMed) ON DELETE CASCADE;

alter table AgendaConsulta ADD FOREIGN KEY(CodCli, CodMed) REFERENCES ClinicaMedico(CodCli, CodMed) ON DELETE CASCADE;

alter table AgendaConsulta ADD FOREIGN KEY(CpfPaciente) REFERENCES Paciente(CpfPaciente) ON DELETE RESTRICT;

DELIMITER $$
CREATE TRIGGER Gatilho_IAAD AFTER INSERT ON Medico
FOR EACH ROW
BEGIN
	INSERT INTO ClinicaMedico values('9999999', NEW.CodMed, NOW(), DEFAULT);
END $$