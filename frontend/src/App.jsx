import { useState } from 'react'
import { io } from "socket.io-client";

import './App.css'

function App() {

  const initial_vals = {
    prevHours: "",
    hourWhenPlayed: "",
    gameType: "",
    playedSolo: "",
    tiredness: "",
    consecutiveWins: "",
  }

  const options = {
    prevHours: [
      { value: "0 - 1 horas", label: "0 - 1 horas" },
      { value: "1 - 2 horas", label: "1 - 2 horas" },
      { value: "2 - 3 horas", label: "2 - 3 horas" },
      { value: "3 - 4 horas", label: "3 - 4 horas" },
      { value: "4 - 5+ horas", label: "4 - 5+ horas" },
    ],
    hourWhenPlayed: [
      { value: "Mañana (6 am - 12 pm)", label: "Mañana (6 am - 12 pm)" },
      { value: "Tarde (12pm - 6pm)", label: "Tarde (12pm - 6pm)" },
      { value: "Noche (6pm - 12am)", label: "Noche (6pm - 12am)" },
      { value: "Madrugada (12am - 6am)", label: "Madrugada (12am - 6am)" },
    ],
    gameType: [
      { value: "MOBA", label: "MOBA" },
      { value: "Shooter", label: "Shooter" },
      { value: "Deportes", label: "Deportes" },
      { value: "Estrategia", label: "Estrategia" },
    ],
    playedSolo: [
      { value: "solo", label: "Solo" },
      { value: "Con amigos", label: "Con amigos" },
    ],
    tiredness: [
      { value: "1", label: "Nada cansado" },
      { value: "2", label: "Poco cansado" },
      { value: "3", label: "Cansado" },
      { value: "4", label: "Muy cansado" },
      { value: "5", label: "Me estoy durmiendo" },
    ],
    consecutiveWins: [
      { value: "1", label: "1" },
      { value: "2", label: "2" },
      { value: "3", label: "3" },
      { value: "4", label: "4" },
      { value: "5", label: "5" },
      { value: "6", label: "6" },
      { value: "7", label: "7" },
      { value: "8", label: "8" },
      { value: "9", label: "9" },
      { value: "10", label: "10+" },
    ],
  };

  const callOnce = (url, event, payload, timeout=5000) =>
  new Promise((resolve, reject) => {
    const socket = io(url, { autoConnect: false, transports: ["websocket"] });
    const t = setTimeout(() => { socket.disconnect(); reject(new Error("timeout")); }, timeout);
    socket.on("connect_error", err => { clearTimeout(t); socket.disconnect(); reject(err); });
    socket.connect();
    socket.emit(event, payload, (ack) => {
      clearTimeout(t);
      resolve(ack);
      socket.disconnect();
    });
  });

  const [form, setForm] = useState(initial_vals);
  const [result, setResult] = useState(null);

    const resetAll = () => {
    setResult(null);
    setForm(initial_vals);
  };

  const setRadio = (name, value) => setForm(f => ({ ...f, [name]: value }));
  const onSubmit = async (e) => {
  e.preventDefault();
  try {
    const res = await callOnce("http://localhost:8000", "process_form", form);
    if (!res?.ok) return alert("error del servidor");
    setResult(res); // { ok, score, label }
  } catch (e) {
    alert("error de socket");
  }
};



  return (
    <div className="shell">
      {!result ? (
      <form onSubmit={onSubmit} className="form">
        <section className="card header">
          <h1 className="title">Predice si ganarás esta sesión</h1>
        </section>

        {/* Horas jugadas antes */}
        <fieldset className="card field" aria-labelledby="lg-horas">
          <legend id="lg-horas" className="legend">¿Cuántas horas llevas jugando? *</legend>
          <div className="options columns-2">
            {options.prevHours.map(o => (
              <label key={o.value} className="option">
                <input
                  type="radio" name="prevHours" value={o.value} required
                  checked={form.prevHours === o.value}
                  onChange={() => setRadio("prevHours", o.value)}
                /> {o.label}
              </label>
            ))}
          </div>
        </fieldset>

        {/* Hora del día */}
        <fieldset className="card field" aria-labelledby="lg-hora">
          <legend id="lg-hora" className="legend">¿Qué hora es? *</legend>
          <div className="options columns-2">
            {options.hourWhenPlayed.map(o => (
              <label key={o.value} className="option">
                <input
                  type="radio" name="hourWhenPlayed" value={o.value} required
                  checked={form.hourWhenPlayed === o.value}
                  onChange={() => setRadio("hourWhenPlayed", o.value)}
                /> {o.label}
              </label>
            ))}
          </div>
        </fieldset>

        {/* Tipo de juego */}
        <fieldset className="card field" aria-labelledby="lg-tipo">
          <legend id="lg-tipo" className="legend">¿Qué tipo de juego estás jugando? *</legend>
          <div className="options columns-2">
            {options.gameType.map(o => (
              <label key={o.value} className="option">
                <input
                  type="radio" name="gameType" value={o.value} required
                  checked={form.gameType === o.value}
                  onChange={() => setRadio("gameType", o.value)}
                /> {o.label}
              </label>
            ))}
          </div>
        </fieldset>

        {/* Solo o con amigos */}
        <fieldset className="card field" aria-labelledby="lg-solo">
          <legend id="lg-solo" className="legend">¿Estás jugando solo o con amigos *</legend>
          <div className="options columns-2">
            {options.playedSolo.map(o => (
              <label key={o.value} className="option">
                <input
                  type="radio" name="playedSolo" value={o.value} required
                  checked={form.playedSolo === o.value}
                  onChange={() => setRadio("playedSolo", o.value)}
                /> {o.label}
              </label>
            ))}
          </div>
        </fieldset>

        {/* Cansancio */}
        <fieldset className="card field" aria-labelledby="lg-cansancio">
          <legend id="lg-cansancio" className="legend">Del 1 - 5 ¿Qué tan cansado estás? *</legend>
          <div className="options columns-4">
            {options.tiredness.map(o => (
              <label key={o.value} className="option">
                <input
                  type="radio" name="tiredness" value={o.value} required
                  checked={form.tiredness === o.value}
                  onChange={() => setRadio("tiredness", o.value)}
                /> {o.label}
              </label>
            ))}
          </div>
        </fieldset>

        {/* Racha */}
        <fieldset className="card field" aria-labelledby="lg-rachas">
          <legend id="lg-rachas" className="legend">¿Cuántas partidas ganadas llevas?  *</legend>
          <div className="options columns-4">
            {options.consecutiveWins.map(o => (
              <label key={o.value} className="option">
                <input
                  type="radio" name="consecutiveWins" value={o.value} required
                  checked={form.consecutiveWins === o.value}
                  onChange={() => setRadio("consecutiveWins", o.value)}
                /> {o.label}
              </label>
            ))}
          </div>
        </fieldset>

        <div className="card actions">
          <button type="submit" className="btn primary">Enviar</button>
          <button type="button" className="btn" onClick={() => setForm(initial_vals)}>Limpiar</button>
        </div>
      </form>

        ) : (

      <section className="card results">

          <h2>K Nearest Neighbors</h2>
          <div className="kpi">Probabilidad de ganar: {result.knnp1}% | Probabilidad de perder: {result.knnp0}%</div>

          <h2>Regresión Logística</h2>
          <div className="kpi">Probabilidad de ganar: {result.logregp1}% | Probabilidad de perder: {result.logregp0}%</div>

          <h2>Naive Bayes</h2>
          <div className="kpi">Probabilidad de ganar: {result.nbp1}% | Probabilidad de perder: {result.nbp0}%</div>

          <div className="actions" style={{ marginTop: 12 }}>
            <button type="button" className="btn primary" onClick={resetAll}>Nueva predicción</button>
          </div>
        </section>

    )}

    </div>
  );

}

export default App
