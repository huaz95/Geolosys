package com.oitsjustjose.geolosys.api;

import java.util.ArrayList;

import com.oitsjustjose.geolosys.common.world.PlutonRegistry;
import com.oitsjustjose.geolosys.common.world.capability.IPlutonCapability;

import net.minecraft.block.BlockState;
import net.minecraftforge.common.capabilities.Capability;
import net.minecraftforge.common.capabilities.CapabilityInject;

/**
 * The Geolosys API is intended for use by anyone who wants to tap into all the locations that deposits exist Access is pretty
 * easy, just reference this class's currentWorldDeposits HashMap
 */
public class GeolosysAPI
{
        @CapabilityInject(IPlutonCapability.class)
        public static final Capability<IPlutonCapability> PLUTON_CAPABILITY = null;
        // A collection of BlockStates that can trigger the prospector's pick
        public static ArrayList<BlockState> proPickExtras = new ArrayList<>();
        // A collection of blocks to ignore in the OreConverter feature
        public static ArrayList<BlockState> oreConverterBlacklist = new ArrayList<>();
        // An instance of the registry for all generatable plutons
        public static PlutonRegistry plutonRegistry = new PlutonRegistry();
}