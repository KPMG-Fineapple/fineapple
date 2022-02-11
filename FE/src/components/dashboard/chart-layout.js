import {
  Box,
  Button,
  Card,
  CardContent,
  CardHeader,
  Divider,
} from "@mui/material";
import ArrowRightIcon from "@mui/icons-material/ArrowRight";

export const ChartLayout = (props) => {
  const { children, allowToggleBtn, title, changeViewMode, viewMode } = props;

  return (
    <Card {...props}>
      <CardHeader
        action={
          allowToggleBtn ? (
            <Button size="small" onClick={() => changeViewMode()}>
              {viewMode === "month" ? "일 별로 보기" : "월 별로 보기"}
            </Button>
          ) : (
            ""
          )
        }
        title={
          allowToggleBtn
            ? viewMode === "month"
              ? "최근 1년 간 전기 사용량"
              : "최근 30일 간 전기 사용량"
            : title
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
