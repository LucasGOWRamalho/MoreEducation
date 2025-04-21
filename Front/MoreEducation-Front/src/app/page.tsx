'use client';
import { useState } from 'react';



const keys = [
  ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
  ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
  ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
  ['ESPACO', 'APAGAR']
];

export default function TecladoPage() {
  const [output, setOutput] = useState('');
  const [highlight, setHighlight] = useState(''); 

  const handleKeyPress = (key: string) => {
    if (key === 'APAGAR') {
      setOutput(prev => prev.slice(0, -1));
    } else if (key === 'ESPACO') {
      setOutput(prev => prev + ' ');
    } else {
      setOutput(prev => prev + key);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8 flex flex-col items-center justify-center gap-8">
      <h1 className="text-3xl font-bold">Teclado Acessível</h1>

      <div className="bg-white rounded-xl shadow-lg p-6 w-full max-w-2xl text-xl border">
        <p className="text-gray-700">{output || 'Digite algo com os olhos...'}</p>
      </div>

      <div className="flex flex-col gap-3">
        {keys.map((row, rowIndex) => (
          <div key={rowIndex} className="flex justify-center gap-2">
            {row.map((key) => (
              <button
                key={key}
                onClick={() => handleKeyPress(key)}
                className={`text-lg px-4 py-2 rounded-xl shadow-sm transition 
                  ${highlight === key ? 'bg-blue-500 text-white' : 'bg-gray-200 hover:bg-gray-300'}`}
              >
                {key === 'ESPACO' ? '␣' : key === 'APAGAR' ? '⌫' : key}
              </button>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}
