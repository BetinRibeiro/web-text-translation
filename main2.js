class TraducaoJSON {
  constructor(jsonArray) {
    this.jsonArray = jsonArray;
  }

  traduzirJSON() {
    const resultado = this.jsonArray.map(item => {
      const chave = Object.keys(item)[0]; // Obtém a chave do objeto
      const traducao = item[chave].traducao;
      const ocorrencia = item[chave].ocorrencia;
      
      return {
        chave: chave,
        traducao: traducao,
        ocorrencia: ocorrencia
      };
    });

    return resultado;
  }

  inserirNaTabela() {
    const dados = this.traduzirJSON();
    const tabela = document.getElementById("dados");
    
    dados.forEach(item => {
      const linha = document.createElement("tr");
      const colunaChave = document.createElement("td");
      colunaChave.textContent = item.chave;
      const colunaTraducao = document.createElement("td");
      colunaTraducao.textContent = item.traducao;
      const colunaOcorrencia = document.createElement("td");
      colunaOcorrencia.textContent = item.ocorrencia;
      
      linha.appendChild(colunaChave);
      linha.appendChild(colunaTraducao);
      linha.appendChild(colunaOcorrencia);
      
      tabela.appendChild(linha);
    });
  }
}

// Função para carregar JSON de uma URL
async function carregarJSONDaURL(url) {
  try {
    const response = await fetch(url);
    if (response.ok) {
      const jsonData = await response.json();
      return jsonData;
    } else {
      console.error("Erro ao obter JSON da URL.");
      return [];
    }
  } catch (error) {
    console.error("Erro ao obter JSON da URL:", error);
    return [];
  }
}

// URL do JSON
const urlJSON = "https://raw.githubusercontent.com/BetinRibeiro/web-text-translation/main/dicionario_ordenado.json";

// Exemplo de uso:
carregarJSONDaURL(urlJSON)
  .then(jsonArray => {
    const traducaoJSON = new TraducaoJSON(jsonArray);
    traducaoJSON.inserirNaTabela();
  })
  .catch(error => {
    console.error("Erro ao carregar o JSON da URL:", error);
  });
