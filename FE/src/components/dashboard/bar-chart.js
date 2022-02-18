import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import { ChartLayout } from "./chart-layout";

export const CustomBarChart = (props) => {
  const { result } = props;
  const keys = Object.keys(result);

  return (
    <ChartLayout {...props}>
      <ResponsiveContainer>
        <BarChart
          data={[result]}
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
          <Bar dataKey={keys[1]} fill="#8884d8" />
          <Bar dataKey={keys[2]} fill="#82ca9d" />
        </BarChart>
      </ResponsiveContainer>
    </ChartLayout>
  );
};
