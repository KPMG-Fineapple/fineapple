import {
  Box,
  Button,
  Card,
  CardContent,
  CardHeader,
  Divider,
} from "@mui/material";
import { useState } from "react";
import ArrowRightIcon from "@mui/icons-material/ArrowRight";

export const ChartLayout = (props) => {
  const [viewMode, setViewMode] = useState("month");
  const { children } = props;

  const changeViewMode = () => {
    const mode = viewMode === "month" ? "day" : "month";
    setViewMode(mode);
  };

  return (
    <Card {...props}>
      <CardHeader
        action={
          <Button size="small" onClick={() => changeViewMode()}>
            {viewMode === "month" ? "일 별로 보기" : "월 별로 보기"}
          </Button>
        }
        title={
          viewMode === "month"
            ? "최근 1년 간 전기 사용량"
            : "최근 30일 간 전기 사용량"
        }
      />
      <Divider />
      <CardContent>
        <Box
          sx={{
            height: 400,
            position: "relative",
          }}
        >
          {children}
        </Box>
      </CardContent>
      <Divider />
      <Box
        sx={{
          display: "flex",
          justifyContent: "flex-end",
          p: 2,
        }}
      >
        <Button
          color="primary"
          endIcon={<ArrowRightIcon fontSize="small" />}
          size="small"
        >
          Overview
        </Button>
      </Box>
    </Card>
  );
};
