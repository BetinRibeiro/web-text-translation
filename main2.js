class TraducaoJSON {
  constructor(jsonArray) {
    this.jsonArray = jsonArray; // Armazena o array de objetos JSON na instância da classe
  }

  traduzirJSON() {
    const resultado = this.jsonArray.map(item => { // Mapeia cada objeto do array JSON
      const chave = Object.keys(item)[0]; // Obtém a primeira chave do objeto
      const traducao = item[chave].traducao; // Acessa a propriedade 'traducao' do objeto
      const ocorrencia = item[chave].ocorrencia; // Acessa a propriedade 'ocorrencia' do objeto
      
      return {
        chave: chave,
        traducao: traducao,
        ocorrencia: ocorrencia
      }; // Retorna um novo objeto com as propriedades chave, traducao e ocorrencia
    });

    return resultado; // Retorna o array de objetos processados
  }

  inserirNaTabela() {
    const dados = this.traduzirJSON(); // Obtém os dados traduzidos do JSON
    const tabela = document.getElementById("dados"); // Obtém a tabela HTML pelo ID 'dados'
    
    dados.forEach(item => { // Para cada objeto traduzido
      const linha = document.createElement("tr border"); // Cria uma nova linha na tabela
      const colunaChave = document.createElement("td"); // Cria uma coluna para a chave
      colunaChave.textContent = item.chave; // Define o texto da coluna como a chave do objeto
      const colunaTraducao = document.createElement("td"); // Cria uma coluna para a tradução
      colunaTraducao.textContent = item.traducao; // Define o texto da coluna como a tradução do objeto
      const colunaOcorrencia = document.createElement("td"); // Cria uma coluna para a ocorrência
      colunaOcorrencia.textContent = item.ocorrencia; // Define o texto da coluna como a ocorrência do objeto
      
      linha.appendChild(colunaChave); // Adiciona a coluna da chave na linha
      linha.appendChild(colunaTraducao); // Adiciona a coluna da tradução na linha
      linha.appendChild(colunaOcorrencia); // Adiciona a coluna da ocorrência na linha
      
      tabela.appendChild(linha); // Adiciona a linha na tabela HTML
    });
  }
}

// Função para carregar JSON de uma URL
async function carregarJSONDaURL(url) {
  try {
    const response = await fetch(url); // Faz uma requisição para a URL especificada
    if (response.ok) {
      const jsonData = await response.json(); // Converte a resposta para JSON
      return jsonData; // Retorna o JSON obtido
    } else {
      console.error("Erro ao obter JSON da URL."); // Exibe mensagem de erro se a resposta não estiver OK
      return []; // Retorna um array vazio em caso de erro
    }
  } catch (error) {
    console.error("Erro ao obter JSON da URL:", error); // Exibe mensagem de erro se houver uma exceção
    return []; // Retorna um array vazio em caso de erro
  }
}

// URL do JSON
const urlJSON = "https://raw.githubusercontent.com/BetinRibeiro/web-text-translation/main/dicionario_ordenado.json";

// Exemplo de uso:
carregarJSONDaURL(urlJSON)
  .then(jsonArray => {
    const traducaoJSON = new TraducaoJSON(jsonArray); // Cria uma instância de TraducaoJSON com o JSON obtido
    traducaoJSON.inserirNaTabela(); // Chama o método para inserir na tabela os dados traduzidos
  })
  .catch(error => {
    console.error("Erro ao carregar o JSON da URL:", error); // Exibe mensagem de erro caso haja um erro no carregamento do JSON
  });
