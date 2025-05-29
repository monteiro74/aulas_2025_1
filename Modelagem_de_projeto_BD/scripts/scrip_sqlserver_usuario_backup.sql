-- Cria o usupario
CREATE LOGIN UsuarioBackupCafe
WITH PASSWORD = 'SenhaForte123!';

-- associa o usuário ao banco de dados café

USE café;
GO

CREATE USER UsuarioBackupCafe FOR LOGIN UsuarioBackupCafe;


-- fornece permissões para realizar o backup
GRANT BACKUP DATABASE TO UsuarioBackupCafe;
GRANT BACKUP LOG TO UsuarioBackupCafe;

-- para fazer restore, uso o banco master
USE master;
GO

GRANT ALTER ANY DATABASE TO UsuarioBackupCafe;

-- e para retirar permissões "extras"
USE café;
GO

DENY SELECT, INSERT, UPDATE, DELETE, EXECUTE TO UsuarioBackupCafe;
