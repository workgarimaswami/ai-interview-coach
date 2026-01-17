import axios from "axios";

export const analyzeInterview = async (audioBlob) => {
  const formData = new FormData();
  formData.append("audio", audioBlob);

  const res = await axios.post(
    "http://localhost:8000/interview/analyze",
    formData
  );
  return res.data;
};
