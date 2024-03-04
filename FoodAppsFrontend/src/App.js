import logo from './logo.svg';
import './App.css';
import SearchFt from './components/dropdown';
import AppPanels from './components/panels';



function App() {
  return (
    <div className="App">

      <header class= "h1 title">Food App (redo)</header>

      <main className="App-header border-success border-5">
        <section>
          <SearchFt />
        </section>
        <section className="d-flex justify-content-center">
          <AppPanels/>
        </section>
      </main>

  


    </div>
  );
}

export default App;
