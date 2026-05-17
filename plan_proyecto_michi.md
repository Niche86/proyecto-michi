# 🐱 Proyecto Final Django: "¿Qué Michi Eres?"

**Entrega:** 23 de mayo de 2026  
**Framework:** Django  
**Base de datos:** SQLite  

---

## 📌 Problemática

En entornos universitarios de alta exigencia académica, los estudiantes técnicos raramente disponen de herramientas ligeras para reflexionar sobre sus patrones de comportamiento ante el estrés. Esta app utiliza un test de personalidad gamificado para que, de forma anónima y rápida, un grupo pueda identificar tendencias colectivas (ej: alta procrastinación, estrés crónico, confusión constante) y tomar decisiones de ritmo de trabajo.

---

## 🗂️ FASE 1: Estructura y Modelos (Día 1 — ~2 horas)

**Objetivo:** Tener la base de datos funcionando y visible en el Admin.

| Paso | Acción | ¿Dónde? |
|------|--------|---------|
| 1.1 | Crear proyecto Django: `django-admin startproject michiproject` | Terminal |
| 1.2 | Crear app: `python manage.py startapp testmichi` | Terminal |
| 1.3 | Registrar app en `INSTALLED_APPS` | `settings.py` |
| 1.4 | Crear los 3 modelos: `Gato`, `Pregunta`, `Respuesta` | `models.py` |
| 1.5 | Crear superusuario: `python manage.py createsuperuser` | Terminal |
| 1.6 | Registrar modelos en `admin.py` (con `list_display`) | `admin.py` |
| 1.7 | Hacer migraciones: `makemigrations` + `migrate` | Terminal |
| 1.8 | Correr servidor y entrar a `/admin` para ver que todo cargue | Navegador |

**Entregable:** Puedes ver `Gato`, `Pregunta` y `Respuesta` en el panel Admin.

---

## 🗂️ FASE 2: Poblar la Base de Datos (Día 1-2 — ~1.5 horas)

**Objetivo:** Tener contenido real para probar la app.

| Paso | Acción |
|------|--------|
| 2.1 | Crear los **5 gatos** en el Admin (nombre, descripción, URL de imagen/GIF) |
| 2.2 | Crear las **10 preguntas** en el Admin |
| 2.3 | Crear las **30 respuestas** (3 por pregunta), asignando el gato correspondiente en cada una |

**Entregable:** Si entras al Admin, ves 5 gatos, 10 preguntas y 30 respuestas con sus relaciones.

---

## 🗂️ FASE 3: Vistas y Templates del Test (Día 2-3 — ~3 horas)

**Objetivo:** El usuario puede ver las preguntas y enviar sus respuestas.

| Paso | Acción | Referencia del tutorial |
|------|--------|------------------------|
| 3.1 | Crear `urls.py` dentro de la app (`testmichi/urls.py`) | Tutorial 1 |
| 3.2 | Incluir las URLs de la app en `michiproject/urls.py` con `include()` | Tutorial 1 |
| 3.3 | Crear **vista `index`** (`ListView` o función): muestra las 10 preguntas con sus opciones | Tutorial 3 |
| 3.4 | Crear **template `index.html`**: formulario con radio buttons | Tutorial 3 |
| 3.5 | Crear **vista `procesar`** (función, tipo `vote()` del tutorial): recibe POST, extrae los IDs de respuestas | Tutorial 4 |
| 3.6 | Crear **vista `resultado`** (`DetailView`): muestra el gato ganador | Tutorial 3 |

**Entregable:** Puedes entrar a `localhost:8000`, ver el test, marcar opciones y dar "Enviar". Aún no muestra resultado correcto, pero no da error.

---

## 🗂️ FASE 4: Lógica de Puntuación (Día 3 — ~1.5 horas)

**Objetivo:** Calcular qué gato ganó y mostrarlo.

| Paso | Acción |
|------|--------|
| 4.1 | En la vista `procesar`, recoger los IDs enviados por POST |
| 4.2 | Buscar las `Respuesta` correspondientes en la BD (`Respuesta.objects.filter(id__in=...)`) |
| 4.3 | Extraer el `gato` de cada respuesta y contar con `Counter` |
| 4.4 | Encontrar el máximo y resolver empates con `random.choice` |
| 4.5 | Redirigir a la URL del gato ganador (`redirect('resultado', pk=ganador.id)`) |

**Entregable:** Al enviar el formulario, te lleva a una página que muestra el gato ganador con su imagen y descripción.

---

## 🗂️ FASE 5: Tests (Día 4 — ~1.5 horas)

**Objetivo:** Un test que pase y demuestre que la lógica funciona.

| Paso | Acción |
|------|--------|
| 5.1 | Crear `tests.py` con una clase `TestVistaTest` |
| 5.2 | Escribir un test que cree los 5 gatos, 1 pregunta y 3 respuestas en memoria |
| 5.3 | Simular un POST enviando siempre la misma respuesta (mismo gato) |
| 5.4 | Verificar que la respuesta redirige al gato esperado (`assertRedirects`) |

**Entregable:** Corres `python manage.py test` y ves `OK` en verde.

---

## 🗂️ FASE 6: Pulir y Subir a GitHub (Día 4-5 — ~1.5 horas)

| Paso | Acción |
|------|--------|
| 6.1 | Crear repositorio en GitHub |
| 6.2 | Hacer `git init`, `git add .`, `git commit -m "proyecto final"`, `git push origin main` |
| 6.3 | Crear `requirements.txt` (`pip freeze > requirements.txt`) |
| 6.4 | Crear `README.md` explicando: problemática, instalación, uso y URL del despliegue |
| 6.5 | Asegurar que `ALLOWED_HOSTS` esté configurado para producción |

**Entregable:** Repositorio público en GitHub con todo el código.

---

## 🗂️ FASE 7: Despliegue en Render (Día 5 — ~2 horas)

| Paso | Acción |
|------|--------|
| 7.1 | Crear cuenta en [render.com](https://render.com) |
| 7.2 | Conectar con tu repositorio de GitHub |
| 7.3 | Crear un **Web Service**, elegir Python |
| 7.4 | Configurar: `Build Command: pip install -r requirements.txt` |
| 7.5 | Configurar: `Start Command: gunicorn michiproject.wsgi:application` |
| 7.6 | Agregar `gunicorn` a `requirements.txt` si no está |
| 7.7 | Esperar el deploy y copiar la URL pública |

**Entregable:** URL pública funcional. La pruebas desde el celular para confirmar.

---

## 🗂️ FASE 8: Video Demo (Día 6 — ~2 horas)

**Máximo 10 minutos.**

| Minuto | Qué mostrar |
|--------|-------------|
| 0:00-1:00 | Intro: "Hola, este es mi proyecto..." |
| 1:00-2:30 | Demo en vivo: haces el test en la URL desplegada y te sale un gato |
| 2:30-4:30 | Código: muestras `models.py`, la vista `procesar` y el `Counter` |
| 4:30-5:30 | Admin: creas una pregunta nueva en vivo para demostrar que es dinámico |
| 5:30-6:30 | Tests: corres `python manage.py test` en terminal y pasan |
| 6:30-8:00 | Repositorio y despliegue: muestras GitHub y la URL pública |
| 8:00-10:00 | Conclusión: qué aprendiste y por qué resuelve una problemática real |

**Entregable:** Video subido a YouTube (público o oculto) con el link listo.

---

## ✅ Checklist Final de Entrega

- [ ] Código en GitHub (repositorio público)
- [ ] URL pública funcionando (Render o similar)
- [ ] Video demo ≤10 min en YouTube
- [ ] README.md con instrucciones claras

---

## 🐱 Los 5 Gatos

| # | Gato | Descripción | Rol |
|---|------|-------------|-----|
| 1 | **Keyboard Cat** | GIF del gato tocando piano. | El chambeador. Resuelve rápido sin drama. |
| 2 | **Crying Cat** | Gato llorando con cara triste. | El estresado. Todo le sale mal. |
| 3 | **This is Fine Cat** | Perro en llamas... pero adaptado a gato. | El optimista. Ignora el caos. |
| 4 | **Loading Cat** | Gato con spinner de carga en la frente. | El confundido. Procesando... pantalla azul mental. |
| 5 | **Lazy Cat** | Gato durmiendo o sin hacer nada. | El procrastinador. "Eso se hace mañana". |

**Balanceo:** Cada gato aparece exactamente **6 veces** entre las 30 respuestas totales. Todos tienen la misma probabilidad matemática de salir ganador.

---

## 📋 Las 10 Preguntas + 30 Respuestas (para copiar al Admin)

### Pregunta 1: Es medianoche y tu código explotó. ¿Qué haces?
- **A → Keyboard Cat:** Arreglo rápido y sigo sin drama.
- **B → Crying Cat:** Cierro la laptop y me voy a llorar a la cama.
- **C → This is Fine Cat:** "Esto está bien, lo reviso mañana con café".

### Pregunta 2: Tienes parcial mañana y no estudiaste. ¿Tu plan?
- **A → Loading Cat:** Miro el temario con cara de spinner, no sé por dónde empezar.
- **B → Lazy Cat:** No estudié, juego una partida y confío en el azar.
- **C → Keyboard Cat:** Hago un café y tiro respuestas de memoria.

### Pregunta 3: El TransMilenio viene lleno en hora pico. ¿Tú?
- **A → This is Fine Cat:** Espero el siguiente con música, no hay prisa.
- **B → Lazy Cat:** Me devuelvo a casa, no vale la pena el esfuerzo.
- **C → Keyboard Cat:** Me meto como sea, tengo que llegar.

### Pregunta 4: Te toca trabajo en equipo para un proyecto. ¿Cómo actúas?
- **A → Crying Cat:** Me estreso porque nadie hace las cosas como yo quiero.
- **B → Keyboard Cat:** Hago la parte difícil yo solo, es más rápido.
- **C → Loading Cat:** Miro el repositorio, miro el Discord, miro la pantalla... y no entiendo qué toca hacer.

### Pregunta 5: No entiendes un concepto del curso. ¿Qué haces?
- **A → Keyboard Cat:** Busco en Stack Overflow y YouTube hasta entenderlo.
- **B → This is Fine Cat:** Le pregunto al profe sin pena, todos aprendemos.
- **C → Loading Cat:** Leo la explicación 5 veces y sigo sin captar. Mi mente está en buffer.

### Pregunta 6: Deadline en 2 horas y estás en blanco. ¿Reacción?
- **A → Keyboard Cat:** Priorizo lo esencial y trabajo enfocado.
- **B → Crying Cat:** Me congelo, abro redes sociales para evadirme.
- **C → Lazy Cat:** "Es imposible terminar", me recuesto y veo memes.

### Pregunta 7: Tu compañero entregó código spaghetti. ¿Tú?
- **A → This is Fine Cat:** Lo acepto, si funciona no le muevo.
- **B → Keyboard Cat:** Lo reescribo todo porque no soporto el desorden.
- **C → Loading Cat:** Abro el archivo, miro 300 líneas en una función... y cierro el IDE.

### Pregunta 8: Reunión de proyecto domingo 8am. ¿Llegas?
- **A → Crying Cat:** Voy tarde, estresado y con cara de pocos amigos.
- **B → Keyboard Cat:** Llego puntual con lo que me tocaba hecho.
- **C → This is Fine Cat:** Voy relajado, es solo una reunión, no pasa nada.

### Pregunta 9: Fin de semana libre después de una semana pesada. ¿Plan?
- **A → Lazy Cat:** Duermo, veo series y no respondo mensajes.
- **B → This is Fine Cat:** Salgo con amigos y olvido que existe la universidad.
- **C → Keyboard Cat:** Aprovecho para adelantar el proyecto del próximo mes.

### Pregunta 10: Hora de hacer deploy a producción. ¿Cómo procedes?
- **A → Lazy Cat:** Le digo a otro que lo haga, me da pánico romper algo.
- **B → Crying Cat:** Estoy en constante refresh de la página con miedo.
- **C → Loading Cat:** Miro la terminal, miro la documentación, miro la terminal otra vez... y no sé si darle enter.

---

## ✅ Verificación de Balance

| Gato | Apariciones | ¿OK? |
|------|-------------|------|
| Keyboard Cat | 6 | ✅ |
| Crying Cat | 6 | ✅ |
| This is Fine Cat | 6 | ✅ |
| Loading Cat | 6 | ✅ |
| Lazy Cat | 6 | ✅ |

**Total: 30 respuestas. Perfectamente balanceado.**
