# Laboratorio 8 – Análisis de Algoritmos

Repositorio del Laboratorio 8 (UVG).  
Incluye: código de los ejercicios programables, perfiles de ejecución, tablas y gráficas.

## Estructura
- \`src/\`: Implementaciones y perfiles por ejercicio (Ex1, Ex2, Ex3).
- \`scripts/\`: Orquestador para correr todos los perfiles.
- \`results/\`: CSVs y gráficas generadas.
- \`docs/\`: Respuestas teóricas en PDF (lo que se hace a mano / ya hecho), más reporte/portada si aplica.

## Cómo correr todo
1. Crear entorno (opcional) e instalar dependencias:
   \`\`\`bash
   python -m venv .venv && source .venv/bin/activate   # en PowerShell: .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   \`\`\`
2. Ejecutar todos los perfiles:
   \`\`\`bash
   python scripts/profile_all.py
   \`\`\`
3. Ver resultados:
   - CSVs en \`results/ex*/\`
   - Gráficas \`*.png\` en \`results/ex*/\`

## Video de evidencia (<= 10 minutos)
- Enlace (no listado): <Pega aquí el link de YouTube>
- Muestra ejecución de \`profile_all.py\` y revisión de \`results/\`.

## Créditos y consideraciones
- Código de profiling propio.
- Respuestas teóricas colocadas en \`docs/\` como PDF.

