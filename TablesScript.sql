USE [Jano]
GO

/****** Object:  Table [dbo].[PlacesInfo]    Script Date: 8/24/2023 2:37:32 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[PlacesInfo](
	[PlaceCode] [int] NOT NULL,
	[PlaceName] [nvarchar](250) NULL,
	[PlaceScore] [smallint] NULL,
	[PlaceFromPrice] [bigint] NULL,
	[PlaceProvince] [nvarchar](100) NULL,
	[PlaceCity] [nvarchar](100) NULL,
	[PlaceNeighborhood] [nvarchar](150) NULL,
	[PlaceM2] [smallint] NULL,
	[PlaceRooms] [nvarchar](30) NULL,
	[PlaceCapacity] [tinyint] NULL,
	[PlaceBuildingType] [nvarchar](150) NULL,
	[PlaceRentalType] [nvarchar](150) NULL,
	[PlaceSecurityType] [nvarchar](150) NULL,
	[PlaceExtraPersonCost] [bigint] NULL,
	[LastUpdate] [datetime] NULL,
 CONSTRAINT [PK_PlacesInfo] PRIMARY KEY CLUSTERED 
(
	[PlaceCode] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

-----------------------------------------------------------------------------------------------------------------

USE [Jano]
GO

/****** Object:  Table [dbo].[PlaceCalendarInfo]    Script Date: 8/24/2023 2:37:43 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[PlaceCalendarInfo](
	[PlaceCode] [int] NOT NULL,
	[DateCode] [nvarchar](10) NOT NULL,
	[Year] [smallint] NULL,
	[Month] [tinyint] NULL,
	[Day] [tinyint] NULL,
	[Price] [bigint] NULL,
	[Currency] [nvarchar](50) NULL,
	[is_holiday] [bit] NULL,
	[is_peek] [bit] NULL,
	[is_unavailable] [bit] NULL,
	[is_promoted_day] [bit] NULL,
	[is_non_bookable] [bit] NULL,
 CONSTRAINT [PK_PlaceCalendarInfo] PRIMARY KEY CLUSTERED 
(
	[PlaceCode] ASC,
	[DateCode] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

