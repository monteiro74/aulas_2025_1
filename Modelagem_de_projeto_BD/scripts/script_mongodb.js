// ============================================
// 1. Selecionar (ou criar) o banco de dados
// ============================================
use local;

db.createCollection("alunos");

//use universidade;

// ============================================
// 2. Criar a collection "alunos" (MongoDB cria automaticamente com o primeiro insert)
// ============================================
// Definindo a estrutura com validação (opcional)
db.createCollection("alunos", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["matricula", "nome", "cpf", "idade", "sexo", "data_nascimento"],
      properties: {
        matricula: { bsonType: "string" },
        nome: { bsonType: "string" },
        cpf: { bsonType: "string" },
        idade: { bsonType: "int" },
        sexo: { bsonType: "string", enum: ["M", "F"] },
        data_nascimento: { bsonType: "date" }
      }
    }
  }
});

// ============================================
// 3. Inserir 5 registros fictícios
// ============================================
db.alunos.insertMany([
  {
    matricula: "A001",
    nome: "João Silva",
    cpf: "11111111111",
    idade: 22,
    sexo: "M",
    data_nascimento: ISODate("2002-01-15")
  },
  {
    matricula: "A002",
    nome: "Maria Oliveira",
    cpf: "22222222222",
    idade: 19,
    sexo: "F",
    data_nascimento: ISODate("2005-06-22")
  },
  {
    matricula: "A003",
    nome: "Carlos Souza",
    cpf: "33333333333",
    idade: 24,
    sexo: "M",
    data_nascimento: ISODate("2000-04-10")
  },
  {
    matricula: "A004",
    nome: "Ana Paula",
    cpf: "44444444444",
    idade: 21,
    sexo: "F",
    data_nascimento: ISODate("2003-09-05")
  },
  {
    matricula: "A005",
    nome: "Bruno Costa",
    cpf: "55555555555",
    idade: 18,
    sexo: "M",
    data_nascimento: ISODate("2006-02-28")
  }
]);

// ============================================
// 4. Buscar alunos pelo nome (exemplo: "João Silva")
// ============================================
db.alunos.find({ nome: "João Silva" });

// ============================================
// 5. Buscar alunos com idade maior que 20 anos
// ============================================
db.alunos.find({ idade: { $gt: 20 } });

// ============================================
// 6. Deletar um aluno com matrícula igual a "A003"
// ============================================
db.alunos.deleteOne({ matricula: "A003" });


// 7. Pesquisa o conteúdo de alunos
db.getCollection("alunos").find({})