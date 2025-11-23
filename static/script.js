document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('password-input');
    const checkBtn = document.getElementById('check-btn');
    const generateBtn = document.getElementById('generate-btn');
    const resultsSection = document.getElementById('results-section');
    const scoreValue = document.getElementById('score-value');
    const feedbackText = document.getElementById('feedback-text');
    const entropyValue = document.getElementById('entropy-value');
    const statusValue = document.getElementById('status-value');
    const scoreCircle = document.querySelector('.score-circle');

    // Función para evaluar contraseña
    async function evaluatePassword() {
        const password = passwordInput.value;
        if (!password) return;

        try {
            const response = await fetch('/api/evaluar', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ password: password })
            });

            const data = await response.json();

            // Actualizar UI
            scoreValue.textContent = data.puntaje;
            feedbackText.textContent = data.feedback;
            entropyValue.textContent = `${data.entropia} bits`;

            if (data.es_comun) {
                statusValue.textContent = "Insegura (Común)";
                statusValue.style.color = "var(--danger)";
                scoreCircle.style.borderColor = "var(--danger)";
            } else if (data.puntaje < 40) {
                statusValue.textContent = "Débil";
                statusValue.style.color = "var(--warning)";
                scoreCircle.style.borderColor = "var(--warning)";
            } else if (data.puntaje < 70) {
                statusValue.textContent = "Decente";
                statusValue.style.color = "var(--accent-primary)";
                scoreCircle.style.borderColor = "var(--accent-primary)";
            } else {
                statusValue.textContent = "Muy Segura";
                statusValue.style.color = "var(--success)";
                scoreCircle.style.borderColor = "var(--success)";
            }

            resultsSection.classList.remove('hidden');
            resultsSection.style.opacity = 1;

        } catch (error) {
            console.error('Error:', error);
            alert('Hubo un error al conectar con el laboratorio.');
        }
    }

    // Función para generar contraseña
    async function generatePassword(e) {
        e.preventDefault();
        try {
            const response = await fetch('/api/generar');
            const data = await response.json();

            passwordInput.value = data.password;
            // Evaluar automáticamente la generada
            evaluatePassword();
        } catch (error) {
            console.error('Error:', error);
        }
    }

    // Event Listeners
    if (checkBtn) {
        checkBtn.addEventListener('click', evaluatePassword);
    }

    if (passwordInput) {
        passwordInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') evaluatePassword();
        });
    }

    if (generateBtn) {
        generateBtn.addEventListener('click', generatePassword);
    }

    console.log("Script loaded v3 - Fixed Null Checks");

    /* --- DEMO LOGIC FOR ROLE PAGES --- */

    // 1. Database Demo: Live Hashing
    const dbInput = document.getElementById('db-demo-input');
    const dbHashOutput = document.getElementById('db-hash-output');
    const dbWarning = document.getElementById('db-warning');

    if (dbInput) {
        dbInput.addEventListener('input', async () => {
            const text = dbInput.value;
            if (!text) {
                dbHashOutput.textContent = "(Esperando entrada...)";
                dbWarning.classList.add('hidden');
                return;
            }

            // Calculate SHA-256
            const msgBuffer = new TextEncoder().encode(text);
            const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
            const hashArray = Array.from(new Uint8Array(hashBuffer));
            const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');

            dbHashOutput.textContent = hashHex;

            // Simple client-side check for demo purposes
            const common = ["123456", "password", "qwerty", "hola", "admin"];
            if (common.includes(text.toLowerCase())) {
                dbWarning.classList.remove('hidden');
            } else {
                dbWarning.classList.add('hidden');
            }
        });
    }

    // 2. Evaluator Demo: Checklist
    const evalInput = document.getElementById('eval-demo-input');
    if (evalInput) {
        evalInput.addEventListener('input', () => {
            const pwd = evalInput.value;

            // Rules
            document.getElementById('check-len').classList.toggle('active', pwd.length >= 8);
            document.getElementById('check-num').classList.toggle('active', /\d/.test(pwd));
            document.getElementById('check-sym').classList.toggle('active', /[!@#$%^&*()_+]/.test(pwd));
            document.getElementById('check-upper').classList.toggle('active', /[A-Z]/.test(pwd) && /[a-z]/.test(pwd));

            // Entropy Sim
            let pool = 0;
            if (/[a-z]/.test(pwd)) pool += 26;
            if (/[A-Z]/.test(pwd)) pool += 26;
            if (/\d/.test(pwd)) pool += 10;
            if (/[^a-zA-Z0-9]/.test(pwd)) pool += 32;

            const entropy = pwd.length * Math.log2(Math.max(1, pool));
            const width = Math.min(100, (entropy / 80) * 100);

            document.getElementById('entropy-bar').style.width = `${width}%`;
            document.getElementById('entropy-text').textContent = `${Math.round(entropy)} bits`;
        });
    }

    // 3. Storage Demo: Log Table
    const btnSaveLog = document.getElementById('btn-save-log');
    const storageInput = document.getElementById('storage-input');
    const logBody = document.getElementById('log-body');

    if (btnSaveLog) {
        btnSaveLog.addEventListener('click', () => {
            const val = storageInput.value;
            if (!val) return;

            const row = document.createElement('tr');
            const time = new Date().toLocaleTimeString();
            row.innerHTML = `
                <td>${time}</td>
                <td>${val}</td>
                <td style="color: var(--success)">Guardado</td>
            `;
            logBody.prepend(row);
            storageInput.value = "";
        });
    }

    // 4. Interface Demo: Flow Animation
    const btnFlow = document.getElementById('btn-flow-start');
    const packet = document.getElementById('packet');
    const flowStatus = document.getElementById('flow-status');
    const nodes = ['node-user', 'node-api', 'node-logic', 'node-db'];

    if (btnFlow) {
        btnFlow.addEventListener('click', async () => {
            btnFlow.disabled = true;
            packet.style.display = 'block';

            const animateStep = (nodeId, text, leftPercent) => {
                return new Promise(resolve => {
                    flowStatus.textContent = text;
                    document.querySelectorAll('.flow-node').forEach(n => n.classList.remove('active'));
                    document.getElementById(nodeId).classList.add('active');

                    packet.style.transition = "left 1s ease";
                    packet.style.left = leftPercent;

                    setTimeout(resolve, 1000);
                });
            };

            await animateStep('node-user', "Usuario envía petición...", "10%");
            await animateStep('node-api', "API recibe datos...", "35%");
            await animateStep('node-logic', "Evaluando seguridad...", "60%");
            await animateStep('node-db', "Verificando en DB...", "90%");

            flowStatus.textContent = "¡Respuesta enviada al usuario!";
            packet.style.display = 'none';
            document.querySelectorAll('.flow-node').forEach(n => n.classList.remove('active'));
            btnFlow.disabled = false;
        });
    }
});
