import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import { ChartLayout } from "./chart-layout";
import { useState } from "react";

const getMonthData = (result) => {
  const currentMonthData = result.current.map((monthData) => {
    return monthData.value.reduce((acc, cur) => acc + cur);
  });
  const predictMonthData = result.predict.map((monthData) => {
    return monthData.value.reduce((acc, cur) => acc + cur);
  });

  const data = currentMonthData.map((item, idx) => {
    const { date } = result.current[idx];
    return {
      name: `${date.substring(5, date.length)}월`,
      현재: item,
      예측: predictMonthData[idx],
    };
  });

  return data;
};

const getDayData = (result) => {
  const currentDayData = result.current[11].value;
  const predictDayData = result.predict[11].value;

  const data = currentDayData.map((item, idx) => {
    return {
      name: `${idx + 1}일`,
      현재: item,
      예측: predictDayData[idx],
    };
  });

  return data;
};

export const Chart = (props) => {
  const { result } = props;
  const [viewMode, setViewMode] = useState("month");
  const [data, setData] = useState(getMonthData(result));

  const changeViewMode = () => {
    const mode = viewMode === "month" ? "day" : "month";
    setViewMode(mode);
    viewMode === "day"
      ? setData(getMonthData(result))
      : setData(getDayData(result));
  };

  return (
    <ChartLayout changeviewmode={changeViewMode} viewmode={viewMode} {...props}>
      <ResponsiveContainer>
        <LineChart
          data={data}
          margin={{
            top: 5,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line
            type="monotone"
            dataKey="현재"
            stroke="#8884d8"
            activeDot={{ r: 8 }}
          />
          <Line type="monotone" dataKey="예측" stroke="#82ca9d" />
        </LineChart>
      </ResponsiveContainer>
    </ChartLayout>
  );
};
