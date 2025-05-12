# Host: localhost  (Version 8.0.30)
# Date: 2025-04-30 15:34:49
# Generator: MySQL-Front 6.1  (Build 1.26)


#
# Structure for table "alunos_origem"
#

DROP TABLE IF EXISTS `alunos_origem`;
CREATE TABLE `alunos_origem` (
  `CPF` char(11) COLLATE utf8mb3_unicode_ci NOT NULL,
  `NomeAluno` varchar(150) COLLATE utf8mb3_unicode_ci NOT NULL,
  `DataNascimento` date NOT NULL,
  `DataMatricula` date NOT NULL,
  `Matricula` varchar(20) COLLATE utf8mb3_unicode_ci NOT NULL,
  `Observacao` text COLLATE utf8mb3_unicode_ci,
  PRIMARY KEY (`CPF`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

#
# Data for table "alunos_origem"
#

INSERT INTO `alunos_origem` VALUES ('01234567890','João Pedro Araújo','2000-11-22','2019-04-10','MAT010','Concluiu estágio obrigatório em 2022.'),('12345678901','Ana Carolina Souza','2002-05-15','2021-03-01','MAT001','Aluno transferido de outra instituição.'),('23456789012','Bruno Henrique Lima','2001-08-20','2020-02-15','MAT002','Participa do projeto de iniciação científica.'),('34567890123','Carlos Eduardo Pinto','2003-11-30','2022-01-10','MAT003','Sem observações.'),('45678901234','Daniela Martins Costa','2002-01-25','2021-08-05','MAT004','Aluno bolsista.'),('56789012345','Eduardo Silva Mendes','2000-07-12','2019-09-20','MAT005','Participou do intercâmbio acadêmico.'),('67890123456','Fernanda Almeida Rocha','2001-04-18','2020-07-15','MAT006','Voluntária no programa de extensão.'),('78901234567','Gabriel Oliveira Santos','2002-12-02','2021-02-22','MAT007','Atleta representando a instituição.'),('89012345678','Helena Ribeiro Castro','2003-03-10','2022-03-01','MAT008','Necessita atendimento pedagógico especial.'),('90123456789','Isabela Fernandes Luz','2001-09-05','2020-08-17','MAT009','Transferido de outra unidade.');
