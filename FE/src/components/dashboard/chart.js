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

export const Chart = (props) => {
  const { result, allowtoggle } = props;
  const keys =
    allowtoggle === "on"
      ? Object.keys(result.months[0])
      : Object.keys(result[0]);
  const [viewMode, setViewMode] = useState("month");
  const [data, setData] =
    allowtoggle === "on" ? useState(result.months) : useState(result);

  const changeViewMode = () => {
    const mode = viewMode === "month" ? "day" : "month";
    setViewMode(mode);
    viewMode === "day" ? setData(result.months) : setData(result.days);
    console.log(result.days);
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
            dataKey={keys[1]}
            stroke="#8884d8"
            strokeWidth={3}
            dot={false}
          />
          <Line
            type="monotone"
            dataKey={keys[2]}
            stroke="#82ca9d"
            strokeWidth={3}
            dot={false}
          />
        </LineChart>
      </ResponsiveContainer>
    </ChartLayout>
  );
};
