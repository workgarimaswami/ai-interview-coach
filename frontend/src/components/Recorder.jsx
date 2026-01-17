import React, { useState } from "react";
import { analyzeInterview } from "../services/api";

export default function Recorder() {
  const [result, setResult] = useState(null);

  const handleUpload = async (e) => {
    const audio = e.target.files[0];
    const data = await analyzeInterview(audio);
    setResult(data);
  };

  return (
    <div>
      <input type="file" accept="audio/*" onChange={handleUpload} />
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}
