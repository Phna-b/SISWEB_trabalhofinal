let chartInstance = null;  // Variável para armazenar o gráfico

        // Função para carregar os anos disponíveis
        async function carregarAnos() {
            const response = await fetch('/dados_treinos');
            const data = await response.json();

            // Extrair anos únicos dos dados disponíveis
            const anosDisponiveis = [...new Set(data.labels.map(label => label.split('-')[0]))].sort();

            const select = document.getElementById('anoSelect');
            select.innerHTML = "";  // Limpa o seletor

            // Adicionar anos disponíveis ao seletor
            anosDisponiveis.forEach(ano => {
                const option = document.createElement('option');
                option.value = ano;
                option.textContent = ano;
                select.appendChild(option);
            });

            // Seleciona o último ano por padrão
            select.value = anosDisponiveis[anosDisponiveis.length - 1];

            // Carrega os dados do ano selecionado
            carregarDados();
        }

        // Função para carregar os dados do servidor e atualizar o gráfico
        async function carregarDados() {
            const anoSelecionado = document.getElementById('anoSelect').value;
            const response = await fetch(`/dados_treinos?ano=${anoSelecionado}`);
            const data = await response.json();

            const ctx = document.getElementById('graficoTreinos').getContext('2d');

            // Se o gráfico já existir, destrua-o para criar um novo
            if (chartInstance) {
                chartInstance.destroy();
            }

            // Criar um novo gráfico
            chartInstance = new Chart(ctx, {
                type: 'bar',  // Gráfico de colunas
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Número de Treinos',
                        data: data.valores,
                        backgroundColor: 'rgba(54, 162, 235, 0.6)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        }

        // Chamar a função para carregar os anos ao carregar a página
        carregarAnos();


        //////////////////////////////////////////////////////////
        //////////////////////////////////////////////////////////
        //////////////////////////////////////////////////////////
        let chartInstance1 = null;  // Variável para armazenar o gráfico

        // Função para carregar as atividades disponíveis
        async function carregarAtividades1() {
            const response = await fetch('/dados_evolucao_carga');
            const data = await response.json();

            const select = document.getElementById('atividadeSelect');
            select.innerHTML = "";  // Limpa o seletor

            // Adicionar a opção padrão "Todas"
            const optionAll = document.createElement('option');
            optionAll.value = "";
            optionAll.textContent = "Todas";
            select.appendChild(optionAll);

            // Adicionar atividades disponíveis ao seletor
            data.atividades.forEach(nome => {
                const option = document.createElement('option');
                option.value = nome;
                option.textContent = nome;
                select.appendChild(option);
            });

            // Carrega os dados da atividade selecionada
            carregarDados1();
        }

        // Função para carregar os dados do servidor e atualizar o gráfico
        async function carregarDados1() {
            const atividadeSelecionada = document.getElementById('atividadeSelect').value;
            const url = atividadeSelecionada ? `/dados_evolucao_carga?nome=${atividadeSelecionada}` : '/dados_evolucao_carga';

            const response = await fetch(url);
            const data = await response.json();

            const ctx = document.getElementById('graficoCargas').getContext('2d');

            // Se o gráfico já existir, destrua-o para criar um novo
            if (chartInstance1) {
                chartInstance1.destroy();
            }

            // Criar um novo gráfico de linha
            chartInstance1 = new Chart(ctx, {
                type: 'line',  // Gráfico de linha para evolução das cargas
                data: {
                    labels: data.labels,  // Atividades registradas (ex: "Atividade 1", "Atividade 2")
                    datasets: [{
                        label: 'Carga Utilizada (kg)',
                        data: data.valores,  // Carga de cada atividade
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 2,
                        fill: true,
                        tension: 0.3  // Suaviza as curvas da linha
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Carga (kg)'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Registro das Atividades'
                            }
                        }
                    }
                }
            });
        }

        // Chamar a função para carregar as atividades ao carregar a página
        carregarAtividades1();
 console.log('Passei aqui')