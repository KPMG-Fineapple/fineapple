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
  const { children, allowtoggle, title, changeviewmode, viewmode } = props;

  return (
    <Card {...props}>
      <CardHeader
        action={
          allowtoggle === "on" ? (
            <Button size="small" onClick={() => changeviewmode()}>
              {viewmode === "month" ? "일 별로 보기" : "월 별로 보기"}
            </Button>
          ) : (
            ""
          )
        }
        title={title}
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
