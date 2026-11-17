import { BrowserRouter, Routes, Route } from "react-router-dom";
import { CaissePage } from "./features/caissiere";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<CaissePage />} />
      </Routes>
    </BrowserRouter>
  );
}